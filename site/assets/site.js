/* Dialectic Skills project page: the surface switch, the install panels, copy buttons, reveals and the film. */
(() => {
  'use strict';

  /* ---------- where do you use it? ---------- */
  const SURFACES = [
    { key: 'claude', label: 'claude.ai' },
    { key: 'code', label: 'Claude Code' },
    { key: 'mobile', label: 'Claude mobile' },
    { key: 'codex', label: 'Codex' },
    { key: 'chatgpt', label: 'ChatGPT' },
  ];
  const startLine = (surface, skill, codex) => {
    switch (surface) {
      case 'code': return { code: `/dia:${skill}`, note: 'Type it in Claude Code.' };
      case 'mobile': return { code: `/${skill}`, note: 'Type it in full: the / menu on mobile does not list plugin skills.' };
      case 'codex': return {
        code: `$dia:${skill}`,
        note: codex === 'select'
          ? 'Follow it with a space and your request. On Codex this skill never starts on its own; select it this way.'
          : 'Follow it with a space and your request. On Codex it may also start when your request matches it.',
      };
      case 'chatgpt': return { code: `@${skill}`, note: 'Type @, then pick the skill.' };
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

  const plates = [...document.querySelectorAll('.plate[data-skill]')];
  const stages = [...document.querySelectorAll('.stage[data-surface]')];
  const stageFor = { claude: 'claude', code: 'code', mobile: 'mobile', codex: 'codex', chatgpt: 'chatgpt' };

  function render(animate) {
    document.querySelectorAll('.surface').forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.surface === current)));
    plates.forEach((plate) => {
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
  const flash = (button, ok) => {
    const label = button.dataset.label || button.textContent;
    button.dataset.label = label;
    button.textContent = ok ? 'Copied' : 'Select and copy';
    clearTimeout(button._t);
    button._t = setTimeout(() => { button.textContent = label; }, 1600);
  };
  document.querySelectorAll('.code').forEach((box) => {
    const code = box.querySelector('code');
    if (!code) return;
    const b = document.createElement('button');
    b.type = 'button';
    b.className = 'copy';
    b.textContent = 'Copy';
    b.setAttribute('aria-label', `Copy: ${code.textContent}`);
    b.addEventListener('click', async () => flash(b, await copyText(code.textContent)));
    box.append(b);
  });
  document.querySelectorAll('[data-copy]').forEach((b) => {
    b.addEventListener('click', async () => flash(b, await copyText(b.dataset.copy)));
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

  /* ---------- the film plays only in view, never under reduced motion ---------- */
  const calm = matchMedia('(prefers-reduced-motion: reduce)');
  const clips = [...document.querySelectorAll('video[autoplay]')];
  const inView = new Set();
  const sync = (v) => {
    if (calm.matches) return;
    if (inView.has(v)) v.play().catch(() => {}); else v.pause();
  };
  const settle = () => {
    for (const v of clips) {
      if (calm.matches) { v.removeAttribute('autoplay'); v.pause(); }
      else sync(v);
    }
  };
  if ('IntersectionObserver' in window) {
    const watch = new IntersectionObserver((entries) => {
      for (const e of entries) { if (e.isIntersecting) inView.add(e.target); else inView.delete(e.target); sync(e.target); }
    }, { threshold: 0.2 });
    clips.forEach((v) => watch.observe(v));
  }
  settle();
  calm.addEventListener('change', settle);
})();
