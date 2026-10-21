# Project page design records

The project page in `site/` (published to https://ajitta.github.io/dialectic-skills/ by `.github/workflows/pages.yml`) was built with the taste-skill skill (tasteskill v2, direction "One motif") and refined with the impeccable skill (critique, audit, detector, polish).

- `PRODUCT.md` and `DESIGN.md` are impeccable's product and design records for the page. Items marked **(inferred)** were not confirmed by the owner. impeccable reads them from the project root: copy them there before running it again, and move them back afterwards.
- Working files of both skills (`.taste-skill/`, `.impeccable/`) are not committed.
- Gates to keep green after a change: taste-skill `lint.mjs site` and `inspect.mjs site/index.html` (0 FAIL), and `impeccable detect` on `site/` and on the served page (0 findings).
- `site/` is not part of the plugin package: no Hangul there either (spec §6); picture credits are in the page footer and `site/assets/img/credits.json`.
- Keep the `google-site-verification` meta tag in `site/index.html`: Google Search Console verifies the property with it. `site/sitemap.xml` lists the page; update `lastmod` on a content change.
- The skill count appears in the title, the meta, Open Graph and Twitter descriptions, the hero lead and link, the intro facts, the skills heading, the claude.ai "Check" step and `site/assets/og.png`. The og image's lead is set in Source Serif 4 at 30px/39px from x 64, y 390 on the sky ground (#cbe4f2); to change the wording, re-render only that block over the old image at the same position.
- Plates follow the README's skill order and alternate sky and sand from sky (see DESIGN.md, Layout). A new plate copies an existing one: picture in greyscale with `--lift` for a dark source, `loading="lazy"`, intrinsic `width` and `height`, a caption, a credits.json entry (the taste-skill `assets.mjs --get` record) and a footer credit with the source page link. Picture files are about 1200px on the long side and 200-250 KB.
- Run the gates headless on ARM64 Linux by pointing them at a no-sandbox wrapper around the Playwright Chromium: `CHROME_PATH=<wrapper>` for taste-skill's `inspect.mjs`, `PUPPETEER_EXECUTABLE_PATH=<wrapper>` for `npx impeccable detect <url>`. inspect.mjs's one WARN (three typefaces: the system monospace counts) is accepted under the Mono Means Type-This rule.
