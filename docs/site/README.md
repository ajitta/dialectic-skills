# Project page design records

The project page in `site/` (published to https://ajitta.github.io/dialectic-skills/ by `.github/workflows/pages.yml`) was built with the taste-skill skill (tasteskill v2, direction "One motif") and refined with the impeccable skill (critique, audit, detector, polish).

- `PRODUCT.md` and `DESIGN.md` are impeccable's product and design records for the page. Items marked **(inferred)** were not confirmed by the owner. impeccable reads them from the project root: copy them there before running it again, and move them back afterwards.
- Working files of both skills (`.taste-skill/`, `.impeccable/`) are not committed.
- Gates to keep green after a change: taste-skill `lint.mjs site` and `inspect.mjs site/index.html` (0 FAIL), and `impeccable detect` on `site/` and on the served page (0 findings).
- `site/` is not part of the plugin package: no Hangul there either (spec §6); picture credits are in the page footer and `site/assets/img/credits.json`.
- Keep the `google-site-verification` meta tag in `site/index.html`: Google Search Console verifies the property with it. `site/sitemap.xml` lists the page; update `lastmod` on a content change.
