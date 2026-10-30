# Four-pass typography and spacing review · 30 October 2026

Scope: strengthen the existing Alfred skill, preserving the approved fonts, quiet palette, concierge, owner-written positioning and both media modes. This review does not redesign the existing walkthrough or pitch.

## Pass 1 — Baseline application and gap review

A fresh agent used the v0.1 files to specify a phone approval card, a shadcn product page and a Persistent Labs inset/phone pitch. It had to invent role sizes, body leading, control targets, gutters, card padding and form spacing. It also followed the stale whole-slide scaling instruction, yielding roughly 5–8px body text on a 390px phone. The existing font names and artwork were usable; implementation rules were incomplete.

## Pass 2 — Deep shadcn and source review

Read the local shadcn skill plus styling, customization, design-system mapping and specimen guidance; cross-checked official theming, Typeset, Card, font-family, gap and @theme inline documentation.

Adopted: semantic theme roles, shared component recipes, explicit typography tuples, gap-based spacing, aligned control dimensions, slot-aware Card padding, correctly themed portals and rendered type/spacing specimens.

Rejected: copying generic Geist/dark-mode/compact presets over Alfred, putting the heavy display face on every small component title, installing a component library just to review it, or claiming referenced runtime font variables never work. Tailwind documents @theme inline for that case; circular or wrongly scoped variables are the actual failure to prevent.

Font-file inspection confirmed Archivo Black is static 400; Space Grotesk supports 300–700 and JetBrains Mono 100–800. The provided font-face declarations match those files.

## Pass 3 — Decisions and implementation

Added 12 complete type roles, a 4px spacing scale, semantic relationship gaps, 20/24px card padding, 44px controls, 16px input/action text, phone action stacking, slot/padding ownership and explicit host/portal boundaries. The online pitch’s phone reflow through 1000px now takes precedence over whole-slide shrinking; PDF/embedded exports retain the fixed canvas.

Canonical JSON generates portable fonts.css, tokens.css and the optional Tailwind v4 bridge. The specimen demonstrates the type hierarchy, space ladder, normal and long-label approval cards, forms and an isolated host inset. A standard-library contract check detects missing roles/files, malformed spacing, synthetic display weights, CSS drift and broken portable links.

## Pass 4 — Verification and independent application

The fresh application test could specify the three original scenarios without inventing material font, spacing or responsive values. Browser checks passed at 320, 390, 768 and 1440px: the actual font faces loaded, body computed to 16/24px, component titles to 20/28px, Archivo remained 400, card padding/gaps matched the contract and all control targets were at least 44px. Keyboard Tab produced the specified 3px focus outline. At 200% text size, body grew to 32px with no page overflow; the host specimen retained its separate typeface.

A narrow-card edge case led to a container-width stacking rule: actions stack when card content is at most 384px, as well as on small screens. The resulting long-label layouts passed the same focused checks. The static checker also rejected synthetic Archivo weight 900, tiny body copy and undersized targets. All three generated CSS files match the canonical tokens.

The plain-CSS specimen and bridge were reviewed; no React/shadcn application was installed or compiled. These checks do not establish actual mobile Safari behaviour, a complete accessibility audit or bank deployment suitability.

## Primary references

[shadcn theming](https://ui.shadcn.com/docs/theming), [Typeset](https://ui.shadcn.com/docs/typeset), [Card](https://ui.shadcn.com/docs/components/card), [Tailwind theme variables](https://tailwindcss.com/docs/theme#referencing-other-variables), [font-family](https://tailwindcss.com/docs/font-family), [gap](https://tailwindcss.com/docs/gap).

Alfred’s numerical settings are brand decisions established in this review, not universal values required by shadcn or Tailwind.
