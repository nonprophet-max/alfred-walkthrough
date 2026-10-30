---
name: alfred-brand
description: Use when creating or reviewing Alfred-branded presentations, websites, Telegram/product mockups, card concepts, marketing copy or Alfred sections inside a multi-brand document.
metadata:
  version: "0.2"
  status: "provisional"
---

# Alfred brand

Use this provisional v0.2 system for Alfred. The owner selected a mostly black-and-white, print-inspired neo-brutalist direction with isolated bold pink and blue. The current three-page pitch is the visual benchmark; the older three-option style study is exploratory, not the current identity.

## Load what the task needs

- For visual design or a substantial document, read [the brand bible](references/brand-bible.md), then [design tokens](assets/tokens.json). Use the supplied fonts, outlined wordmarks and illustration.
- For typography, spacing or any UI, read [the typography and spacing contract](references/typography-and-spacing.md). It defines complete roles, real font loading, density, control sizing, responsive modes and browser checks. Load `assets/fonts.css` and generated `assets/tokens.css` together.
- For an actual shadcn project, also read [shadcn integration](references/shadcn-integration.md); use the project’s existing components and CSS. The kit does not require shadcn installation for plain HTML or design work.
- For a narrow copy task, read the bible’s **Positioning**, **Voice**, and **Claims** sections.
- For work within Persistent Labs research, read **Mixed-brand documents**. Alfred is an inset product identity; do not restyle the host research, Instinct case study or FireFlow technical surface as Alfred.
- The [asset map](references/assets.md) identifies files and their intended uses. Paths are relative to this skill, with no dependency on the creator’s machine.

## Keep the recognizable decisions

- Ink `#111110`, paper `#F7F7F2`, white `#FFFFFF`. Pink `#FF4FA0` and blue `#1975FF` are isolated flourishes, not competing page-wide themes.
- Archivo Black for the lowercase `alfred` wordmark and large display type; Space Grotesk for readable body copy; JetBrains Mono for labels and metadata. Archivo Black is supplied as a regular-weight font: use weight 400, not synthetic 900.
- Oversized, purposeful headlines; strong black outlines; rounded frames and pills; occasional hard offset shadows. Do not force the earlier square-corner template rules onto this identity.
- Use the supplied little concierge character: black bow tie, white gloves, shoes and everyday task objects. Keep its existing pink/blue details. Treat it as the current signature illustration, not a mandate to place a mascot on every screen.
- The core phrase is **“Life, handled.”** The functional promise is **“Find it. Book it. Buy it.”** Keep the voice capable, warm, direct and lightly playful.

## Make type and spacing reproducible

- Choose named typography roles; each fixes family, weight, size, leading and tracking together. Body is Space Grotesk 400 at 16/24px; component titles are Space Grotesk 600 at 20/28px. Archivo Black remains 400 and is reserved for larger display work and the wordmark.
- Use the 4px spacing scale and semantic relationship gaps. Default card padding is 20px on phones / 24px wider, field groups 24px, label-to-control 8px and actions 12px. A gap has one owner; do not double card/root slot padding.
- Controls are at least 44px, use 16px labels/input text, and may grow for wrapping. Stack phone actions through 479px and narrow-card actions through 384px of available content width. Reserve actual fixed-navigation height plus safe-area space and 16px clearance.
- The JSON is canonical. Run `python3 scripts/build_tokens.py` after token changes, then `python3 scripts/check_contract.py`. Use [the live specimen](assets/examples/type-spacing.html) to inspect the roles and spacing; the check script does not replace a real font/keyboard/mobile review.
- In shadcn, put branding in semantic theme tokens and shared component recipes. Keep per-use className for layout. Do not import generic Geist/dark-mode defaults or global font mappings into a Persistent Labs host.

## Preserve the product distinctions

**Instinct is an external inspiration and market benchmark. Alfred is our proposed product. FireFlow is the proposed architectural foundation.** Do not write as if Instinct belongs to Alfred or transfer Instinct’s financing, users or transaction activity to Alfred.

Alfred’s ambition is a better Telegram-native experience for booking, price search/sourcing and retail purchasing, with an optional branded card and rewards relationship. The same execution core is intended to support consumer distribution and bank-native, co-branded or white-label experiences, including a bank-controlled/on-prem route to validate.

Explain the architectural thesis using durable workflows, bounded permissions, approvals, isolation, auditability and recovery. A conventional chat front end alone does not supply those controls. Do not turn that distinction into a claim that every competing assistant is incapable of banking use, or that Alfred already has bank certification, production deployment or issuer partnerships.

## Apply it to the actual deliverable

Use the existing format, audience and requested scope. A three-page pitch is one example, not the required length of every Alfred artifact. The online pitch has an approved reflowing phone layout through 1000px. Fixed 16:9 PDF/print and embedded slide exports scale as a whole. Ordinary websites and reading documents reflow; do not shrink their body text to fit an entire slide on a phone.

When Alfred appears inside another brand’s document, use the wordmark treatment on its name and scope the Alfred tokens, artwork and components to Alfred product material. Keep surrounding research typography and navigation in the host brand. Preserve separate FireFlow branding inside architecture diagrams.

Use dates and attribution for external market proof. Describe planned functionality as a vision, example or proposed design. Card and purchase illustrations do not establish a live financial programme. Use actual source evidence before making current capability or market claims.

Before delivery, inspect the real output for readable typography, intact logos, restrained accents, text/panel overlap and working navigation. If sharing or deployment is requested, follow the session’s existing authorization; the skill itself grants no additional permission.
