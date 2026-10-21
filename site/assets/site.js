/* Dialectic Skills project page: the surface switch, the install panels, copy buttons, reveals and the film. */
(() => {
  'use strict';

  /* ---------- where do you use it? ---------- */
  const SURFACES = [
    { key: 'code', label: 'Claude Code' },
    { key: 'codex', label: 'Codex' },
    { key: 'claude', label: 'claude.ai / desktop' },
    { key: 'mobile', label: 'Claude mobile' },
    { key: 'chatgpt', label: 'ChatGPT' },
  ];
  const startLine = (surface, skill, codex) => {
    switch (surface) {
      case 'code': return { code: `/dia:${skill}`, note: 'Type it in Claude Code.' };
      case 'mobile': return { code: `/${skill}`, note: 'Type it in full: the / menu on mobile does not list plugin skills.' };
      case 'codex': return {
        code: `$dia:${skill}`,
        note: codex === 'name'
          ? 'Follow it with a space and your request, or start the message with the skill name. It is meant to start only these ways, not from a plain request.'
          : 'Follow it with a space and your request. On Codex it may also start when your request matches it.',
      };
      case 'chatgpt': return { code: `@${skill}`, note: 'Type @, then pick the skill. Since 1.2.0 you can also start the message with the skill name.' };
      default: return { code: `/dia:${skill}`, note: 'Type it in the message box on claude.ai or Claude desktop.' };
    }
  };

  let store = null;
  try { store = window.localStorage; } catch (e) { store = null; }
  const saved = store && store.getItem('dia-surface');
  let current = SURFACES.some((s) => s.key === saved) ? saved : 'claude';

  const groups = [...document.querySelectorAll('.surfaces')];
  groups.forEach((group) => {
    SURFACES.forEach((s) => {
      const b = document.createElement('button');
      b.type = 'button';
      b.className = 'surface';
      b.dataset.surface = s.key;
      b.textContent = s.label;
      b.addEventListener('click', () => choose(s.key, true));
      group.append(b);
    });
  });
  // On narrow screens the same choice is a native select.
  const pickers = [...document.querySelectorAll('.switch__select')];
  pickers.forEach((sel) => {
    SURFACES.forEach((s) => sel.append(new Option(s.label, s.key)));
    sel.addEventListener('change', () => choose(sel.value, true));
  });

  const plates = [...document.querySelectorAll('.plate[data-skill]')];
  // The prompt to try, as README writes it. Since 1.2.0 every prompt works unchanged on Codex too:
  // the dia-confirm and dia-iterate prompts start with the skill name, which Codex now resolves.
  plates.forEach((plate) => {
    const code = plate.querySelector('.try code');
    if (code) plate.dataset.prompt = code.textContent;
  });
  const promptFor = (surface, plate) => plate.dataset.prompt || '';
  const stages = [...document.querySelectorAll('.stage[data-surface]')];
  const stageFor = { claude: 'claude', code: 'code', mobile: 'mobile', codex: 'codex', chatgpt: 'chatgpt' };

  function render(animate) {
    document.querySelectorAll('.surface').forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.surface === current)));
    pickers.forEach((sel) => { sel.value = current; });
    plates.forEach((plate) => {
      const prompt = promptFor(current, plate);
      const tryCode = plate.querySelector('.try code');
      const copyButton = plate.querySelector('[data-copy]');
      if (tryCode && tryCode.textContent !== prompt) tryCode.textContent = prompt;
      if (copyButton) copyButton.dataset.copy = prompt;
      const { code, note } = startLine(current, plate.dataset.skill, plate.dataset.codex);
      const el = plate.querySelector('.start__code');
      const noteEl = plate.querySelector('.start__note');
      if (el && el.textContent !== code) {
        el.textContent = code;
        if (animate) { el.classList.remove('is-new'); void el.offsetWidth; el.classList.add('is-new'); }
      }
      if (noteEl) noteEl.textContent = note;
    });
  }

  function openStage(key) {
    stages.forEach((st) => {
      const open = st.dataset.surface === key;
      st.classList.toggle('is-open', open);
      const btn = st.querySelector('.stage__btn');
      if (btn) btn.setAttribute('aria-expanded', String(open));
    });
  }

  function choose(key, animate) {
    current = key;
    if (store) { try { store.setItem('dia-surface', key); } catch (e) { /* private mode */ } }
    render(animate);
    openStage(stageFor[key]);
  }

  stages.forEach((st) => {
    const btn = st.querySelector('.stage__btn');
    if (!btn) return;
    btn.addEventListener('click', () => {
      if (st.classList.contains('is-open')) return;
      choose(st.dataset.surface, true);
    });
  });

  choose(current, false);

  /* ---------- copy buttons ---------- */
  const copyText = async (text) => {
    try { await navigator.clipboard.writeText(text); return true; }
    catch (e) {
      const ta = document.createElement('textarea');
      ta.value = text; ta.setAttribute('readonly', ''); ta.style.position = 'fixed'; ta.style.opacity = '0';
      document.body.append(ta); ta.select();
      let ok = false;
      try { ok = document.execCommand('copy'); } catch (err) { ok = false; }
      ta.remove();
      return ok;
    }
  };
  const status = document.getElementById('copy-status');
  const selectText = (el) => {
    if (!el) return;
    const range = document.createRange();
    range.selectNodeContents(el);
    const sel = getSelection();
    sel.removeAllRanges();
    sel.addRange(range);
  };
  // Success flashes on the button and is announced; on failure the text is left selected, so the
  // visitor can copy it with the keyboard or the system menu.
  const flash = (button, ok, source) => {
    const label = button.dataset.label || button.textContent;
    button.dataset.label = label;
    button.textContent = ok ? 'Copied' : 'Selected: copy it';
    if (!ok) selectText(source);
    if (status) {
      // Clear first so a repeated message is announced again.
      status.textContent = '';
      const msg = ok ? 'Copied to the clipboard.' : 'Could not copy. The text is selected; copy it with Ctrl+C or Command+C.';
      setTimeout(() => { status.textContent = msg; }, 60);
    }
    clearTimeout(button._t);
    button._t = setTimeout(() => { button.textContent = label; }, ok ? 1600 : 4000);
  };
  document.querySelectorAll('.code').forEach((box) => {
    const code = box.querySelector('code');
    if (!code) return;
    const b = document.createElement('button');
    b.type = 'button';
    b.className = 'copy';
    b.textContent = 'Copy';
    b.setAttribute('aria-label', `Copy: ${code.textContent}`);
    b.addEventListener('click', async () => flash(b, await copyText(code.textContent), code));
    box.append(b);
  });
  document.querySelectorAll('[data-copy]').forEach((b) => {
    const source = b.closest('.plate')?.querySelector('.try code');
    b.addEventListener('click', async () => flash(b, await copyText(b.dataset.copy), source));
  });

  /* ---------- reveals, once ---------- */
  const reveals = [...document.querySelectorAll('[data-reveal]')];
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => {
      for (const e of entries) if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
    }, { rootMargin: '0px 0px -10% 0px', threshold: 0.08 });
    reveals.forEach((el) => io.observe(el));
    // A fast jump (a link, the End key) can carry the page past an element between two frames, and the
    // observer then never sees it intersect: show whatever is already above the fold.
    let queued = false;
    const catchUp = () => {
      queued = false;
      const limit = innerHeight * 0.9;
      for (const el of reveals) {
        if (el.classList.contains('is-in')) continue;
        if (el.getBoundingClientRect().top < limit) { el.classList.add('is-in'); io.unobserve(el); }
      }
    };
    addEventListener('scroll', () => { if (!queued) { queued = true; requestAnimationFrame(catchUp); } }, { passive: true });
  } else {
    reveals.forEach((el) => el.classList.add('is-in'));
  }

  /* ---------- the film plays only in view, never under reduced motion, and can be paused ---------- */
  const calm = matchMedia('(prefers-reduced-motion: reduce)');
  const clips = [...document.querySelectorAll('video[autoplay]')];
  const inView = new Set();
  let held = false; // the visitor paused the film, or reduced motion asks for stillness
  const toggle = document.querySelector('.film__toggle');
  const label = () => { if (toggle) toggle.textContent = held ? 'Play the film' : 'Pause the film'; };
  const sync = (v) => {
    if (held) { v.pause(); return; }
    if (inView.has(v)) v.play().catch(() => {}); else v.pause();
  };
  const settle = () => {
    if (calm.matches) { held = true; clips.forEach((v) => v.removeAttribute('autoplay')); }
    clips.forEach(sync);
    label();
  };
  if (toggle && clips.length) {
    toggle.hidden = false;
    toggle.addEventListener('click', () => { held = !held; clips.forEach(sync); label(); });
  }
  if ('IntersectionObserver' in window) {
    const watch = new IntersectionObserver((entries) => {
      for (const e of entries) { if (e.isIntersecting) inView.add(e.target); else inView.delete(e.target); sync(e.target); }
    }, { threshold: 0.2 });
    clips.forEach((v) => watch.observe(v));
  }
  settle();
  calm.addEventListener('change', settle);
})();
