# Project page design records

The project page in `site/` (published to https://ajitta.github.io/dialectic-skills/ by `.github/workflows/pages.yml`) was built with the taste-skill skill (tasteskill v2, direction "One motif") and refined with the impeccable skill (critique, audit, detector, polish).

- `PRODUCT.md` and `DESIGN.md` are impeccable's product and design records for the page. Items marked **(inferred)** were not confirmed by the owner. impeccable reads them from the project root: copy them there before running it again, and move them back afterwards.
- Working files of both skills (`.taste-skill/`, `.impeccable/`) are not committed.
- Gates to keep green after a change: taste-skill `lint.mjs site` and `inspect.mjs site/index.html` (0 FAIL), and `impeccable detect` on `site/` and on the served page (0 findings).
- `site/` is not part of the plugin package: no Hangul there either (spec §6); picture credits are in the page footer and `site/assets/img/credits.json`.
- Keep the `google-site-verification` meta tag in `site/index.html`: Google Search Console verifies the property with it. `site/sitemap.xml` lists the page; update `lastmod` on a content change.
- By owner decision the page and `site/assets/og.png` carry no skill count, so adding a skill needs only its plate, list entry and picture. The og image's lead is set in Source Serif 4 at 30px/39px from x 64, y 390 on the sky ground (#cbe4f2); to change the wording, re-render only that block over the old image at the same position.
- Plates follow the README's skill order and alternate sky and sand from sky (see DESIGN.md, Layout). A new plate copies an existing one: picture in greyscale with `--lift` for a dark source, `loading="lazy"`, intrinsic `width` and `height`, a caption, a credits.json entry (the taste-skill `assets.mjs --get` record) and a footer credit with the source page link. Picture files are about 1200px on the long side and 200-250 KB; serve them through AVIF and WebP renditions (Pictures, below). The session or output goes in the plate's `<details class="session">` after the buttons, closed (see DESIGN.md, Session toggle).
- Run the gates headless on ARM64 Linux by pointing them at a no-sandbox wrapper around the Playwright Chromium: `CHROME_PATH=<wrapper>` for taste-skill's `inspect.mjs`, `PUPPETEER_EXECUTABLE_PATH=<wrapper>` for `npx impeccable detect <url>`. inspect.mjs's one WARN (three typefaces: the system monospace counts) is accepted under the Mono Means Type-This rule. Where the host asks for reduced motion (Windows with animation effects off), headless Chrome reports `prefers-reduced-motion: reduce` and inspect.mjs fails `still-page`; launch Chrome with `--force-prefers-no-reduced-motion` for that run.

## Pictures

Every picture in `site/assets/img/` is a JPG (the `<img>` fallback and the file credits.json names) plus AVIF and WebP renditions named `<base>-w<width>.avif` and `.webp`. `og.png` and the icons stay as they are: social cards need PNG. The film poster in `site/assets/video/` is a `poster` attribute and stays a JPG.

- **Widths.** 480 and 800 px when that is at most 85% of the source width, and the source width itself (1200 for most, 1400 for the hero). The three intro thumbnails also get 160 px. Measured circles: hero 720 px at 1440 by 900 and 325 px at 375; plates 445 px at 1440 and 147 px at 375; thumbnails 42 px.
- **Regenerate** after adding or replacing a JPG (Pillow 11.2 or later reads and writes AVIF; about a minute for all of them on ARM64). Quality AVIF 55, WebP 78 keeps the circles visually identical to the JPG after the greyscale filter; the ICC profile is carried over.

```sh
cat > /tmp/renditions.py <<'EOF'
import sys, pathlib
from PIL import Image, ImageOps
THUMBS = {'socrates-herm', 'euclid-1482', 'diogenes-lantern'}  # pictures also used as intro thumbnails
folder = pathlib.Path(sys.argv[1])
for jpg in sorted(folder.glob('*.jpg')):
    src = ImageOps.exif_transpose(Image.open(jpg)).convert('RGB')
    icc = Image.open(jpg).info.get('icc_profile')
    W, H = src.size
    widths = [w for w in (480, 800) if w <= 0.85 * W] + [W] + ([160] if jpg.stem in THUMBS else [])
    for w in widths:
        im = src if w == W else src.resize((w, round(H * w / W)), Image.LANCZOS)
        extra = {'icc_profile': icc} if icc else {}
        im.save(folder / f'{jpg.stem}-w{w}.avif', quality=55, speed=4, subsampling='4:2:0', **extra)
        im.save(folder / f'{jpg.stem}-w{w}.webp', quality=78, method=6, **extra)
    print(jpg.name, widths)
EOF
uv run --with 'pillow>=11.2' python /tmp/renditions.py site/assets/img
```

- **Markup.** Wrap the `<img>` (it keeps its class, `src` to the JPG, `width`, `height`, `alt`, `loading`, `decoding` and inline `style`, so the greyscale, `--lift` and `object-position` apply to every format) in `<picture>` with two sources, AVIF first. List the 160 px rendition only in thumbnails, and nothing above 480 in them:

```html
<picture>
  <source type="image/avif" srcset="assets/img/NAME-w480.avif 480w, assets/img/NAME-w800.avif 800w, assets/img/NAME-w1200.avif 1200w" sizes="SIZES">
  <source type="image/webp" srcset="assets/img/NAME-w480.webp 480w, assets/img/NAME-w800.webp 800w, assets/img/NAME-w1200.webp 1200w" sizes="SIZES">
  <img class="pair__a" src="assets/img/NAME.jpg" width="1200" height="900" loading="lazy" decoding="async" style="object-position:50% 50%" alt="...">
</picture>
```

- **`sizes`.** A plate circle is about 31vw wide from 900px, min(45vw, 355px) from 600px and calc(43vw - 14px) below. The circle crops the picture with `object-fit: cover`, so a landscape source must be W/H times wider than the circle: multiply each value by A = max(1, width / height), rounded. The 1200 by 798 Death of Socrates (A = 1.5) gets `(min-width: 900px) 47vw, (min-width: 600px) min(68vw, 534px), calc(65vw - 21px)`; a portrait one gets the plain values. The hero uses `(min-width: 1240px) min(80vh, 54vw), (min-width: 900px) min(80vh, 48vw), (min-width: 600px) 66vw, 87vw` and stays eager (no `loading`) with `fetchpriority="high"`; thumbnails use `sizes="42px"` and sit on one line with no whitespace inside `<picture>`, so the spacing in the sentence does not change.
- **Check** in Chromium at 375 and 1440, DPR 1 and 2, that each `img.currentSrc` is an AVIF of at least the circle's width times A times the DPR (or the largest rendition), and that the circles match the JPG in a screenshot: the mean luminance of each circle moved by less than 0.3 of 255 when this pipeline was introduced.

