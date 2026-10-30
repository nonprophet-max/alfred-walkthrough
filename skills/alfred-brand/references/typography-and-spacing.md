# Alfred typography and spacing contract · v0.2

These are Alfred implementation decisions, informed by the shadcn review. They are not shadcn defaults. `assets/tokens.json` is canonical; `python3 scripts/build_tokens.py` regenerates the portable CSS. Apply current owner instructions over these defaults and record a deliberate exception beside the affected component.

## 1. Load the real fonts

Copy `assets/fonts.css`, `assets/tokens.css` and `assets/fonts/` together. Load fonts.css before tokens.css. Font URLs resolve relative to fonts.css, not to the HTML document. No external font service is required.

| Family | Actual bundled file | Declared weight | Role |
| --- | --- | --- | --- |
| Archivo Black | `archivoblack.ttf` | Static 400 | Wordmark and large editorial/display headings |
| Space Grotesk | `spacegrotesk.ttf` | Variable 300–700 | Body, controls, forms and component headings |
| JetBrains Mono | `jetbrainsmono.ttf` | Variable 100–800 | Short metadata and technical labels |

Do not assign Archivo Black 600/700/900, synthesize bold/italic, replace the typefaces with Geist/Inter, or rely on a fallback as the finished result. Use `font-synthesis: none` on Alfred surfaces. Small `CardTitle`, dialog and form headings use Space Grotesk 600; the heavy display face does not belong on every UI label.

## 2. Web type roles

The generated `.alfred-type-*` classes set all five properties together. Dimensions below assume the browser’s normal 16px root; CSS uses rem, leaves the root size alone and respects text enlargement. Leading is unitless; tracking is in em. Headings grow with clamp() up to the stated maximum.

| Token | Family / weight | Size px | Leading | Tracking em | Use |
| --- | --- | --- | --- | --- | --- |
| hero | Archivo Black 400 | 48–80 | 1.04 | −0.04 | One dominant editorial headline |
| heading | Archivo Black 400 | 36–48 | 1.10 | −0.035 | Main page heading |
| section | Archivo Black 400 | 28–36 | 1.15 | −0.025 | Major section heading |
| component-title | Space Grotesk 600 | 20 | 1.40 | −0.015 | Card, dialog, form-group title |
| lead | Space Grotesk 400 | 20 | 1.50 | 0 | Short introduction |
| body | Space Grotesk 400 | 16 | 1.50 | 0 | Main product text |
| body-small | Space Grotesk 400 | 14 | 1.428571 | 0 | Secondary description and help |
| label | Space Grotesk 600 | 14 | 1.428571 | 0 | Form label |
| control | Space Grotesk 600 | 16 | 1.50 | 0 | Button label |
| input | Space Grotesk 400 | 16 | 1.50 | 0 | Typed input |
| caption | JetBrains Mono 400 | 12 | 1.333333 | +0.04 | Short metadata, not instructions |
| amount | Space Grotesk 600 | 28 | 1.20 | −0.02 | Price or approval amount; tabular figures |

Keep running text at no more than 68ch. Give display headings a deliberate measure, typically 12–18ch, and allow natural wrapping. Body text and controls have zero tracking; do not spread mono labels across paragraphs. Uppercase is for short metadata only. Inline Alfred names inherit the surrounding size/line-height and use the supplied wordmark face at 400, with −0.025em tracking; they must not change the host document’s rhythm.

Never truncate the amount, merchant, terms or required approval instructions to make a card fit. Let height grow. Headline wrapping may be balanced; user instructions and legal/service text remain normally readable.

## 3. Space by relationship

Use a 4px base: **0, 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96**. `--alfred-space-4` is 16px, matching Tailwind’s standard `gap-4`; it is not 4px. Borders, focus outlines and optical artwork placement are separate dimensions.

| Relationship | Default px | Tailwind equivalent / note |
| --- | --- | --- |
| Icon–label, label–control, control–help | 8 | gap-2 |
| Related content inside a group | 16 | gap-4 |
| Action buttons | 12 | gap-3 |
| Field groups / card content groups | 24 | gap-6 |
| Card padding below 768px / wider | 20 / 24 | p-5 / md:p-6 |
| Page gutter below 768px / wider | 20 / 32 | px-5 / md:px-8 |
| Major sections below 768px / wider | 48 / 64 | gap-12 / md:gap-16 |
| Page content maximum | 1200 | A container limit, not a text measure |

Use flex/grid gap for sibling spacing. Each relationship has one owner: do not combine a parent gap with child margins for the same separation. For a padded card, choose one padding owner: Alfred’s default is a root with 20/24px padding and 24px group gaps, with zero child-slot padding. Inspect the installed Card first; remove conflicting built-in root/slot padding in its shared recipe. Never add p-6 to both Card and CardContent by habit.

Default controls and icon-button targets are at least **44×44px**. Buttons and single-line inputs share 44px minimum height, 8px block / 12px inline padding, 2px borders and 12px radii. Buttons may grow when labels wrap; textareas use the same input typography with an expanding height. On screens through 479px, actions stack with a 12px gap. They also stack when their card’s content width is at most 384px, even on a wider screen; a two-column layout must not force long labels into narrow side-by-side buttons. Use readable labels and full-width buttons; do not reduce type or hit area to force a row.

Alfred web panels use 20px radii, 2px ink borders and optional 4px hard shadows. The older 35/26/42px radii and 3/5px borders in `shape` describe the 1920×1080 pitch canvas. Do not apply those slide pixels to every product control.

## 4. Media and host boundaries

- **Standalone product web:** use the roles and semantic spacing above. Minimum reading checks: 320px, 390px, 768px and 1440px, plus enlarged text.
- **Online three-page pitch:** the approved phone mode reflows through 1000px. Preserve the same three sections, words and navigation; use a vertical reading layout instead of scaling all body text down. Desktop keeps the authored composition.
- **PDF/print and embedded slide export:** preserve the 1920×1080 stage and scale the whole composition. Slide type examples (95–198px display, 24–38px body) are canvas coordinates, not phone CSS sizes.
- **Persistent Labs host:** load prefixed tokens and style Alfred’s named/product islands only. Keep host Red Hat typography, navigation and gold/graphite framing. Do not apply a global shadcn font/theme bridge to that document. Keep FireFlow distinct.
- **Fixed bottom controls:** measure the controls’ actual height and reserve content/scroll padding for that height, safe-area inset and at least 16px of separation. The final line, action and footer must scroll fully above the bar. Keep controls visible on chapter changes and orientation changes.

## 5. Prove the result

Wait for `document.fonts.ready`, then explicitly load the relevant family/weight and require a non-empty loaded-face list. `document.fonts.check()` alone can give misleading confidence when no matching face was registered. Check computed family, weight, size, line-height and tracking for real specimens; a CSS family name alone does not prove a font was downloaded.

Check body=16/24px, component title=20/28px, Archivo=400, controls≥44px, correct card padding/gaps, long translated labels, errors/help text, 200% text enlargement and no horizontal overflow. Verify keyboard focus with Tab, not only a screenshot. Inspect the real layout with the web fonts loaded and the last item scrolled above any fixed controls. The package contract check catches missing files or token/CSS drift; it does not replace browser or accessibility review.
