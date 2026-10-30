# From Instinct to Alfred

A Persistent Labs styled research walkthrough, with 15 short chapters and the complete research appendix.

Research dated 29 October 2026; source availability and delivery reviewed 30 October 2026.

Alfred is a proposed product. Consumer, bank/co-brand and optional bank white-label routes are all in scope. Examples do not describe a live service, approved financial programme or bank partnership. Official statements, reporting, interpretation and proposals are distinguished in the guide.

The HTML includes the complete research and embedded fonts. The PDF is an accessible reading copy. Some external source sites require sign-in or restrict automated access; their limits are documented in the walkthrough.

Bundled Red Hat fonts are covered by the included SIL Open Font License notices. The PDF reading copy uses Arial.


## Alfred brand bible and reusable skill

The provisional v0.2 brand kit captures the approved monochrome neo-brutalist direction, isolated pink/blue accents, typefaces, outlined wordmarks, optional card concept and little concierge.

- [Read the brand bible](https://nonprophet-max.github.io/alfred-walkthrough/brand/)
- [Browse the reusable Alfred skill](skills/alfred-brand/SKILL.md)
- [Download the portable skill bundle](https://nonprophet-max.github.io/alfred-walkthrough/brand/alfred-brand-v0.2.zip)
- [Open the three-page pitch](https://nonprophet-max.github.io/alfred-walkthrough/pitch/)

To use in this repository, ask your agent to read `skills/alfred-brand/SKILL.md` and follow its relative references. For installation, unpack the `alfred-brand` folder into your agent’s skills directory, then invoke `$alfred-brand` where supported. The package includes fonts and licence notices; keep its folder structure intact.

The research walkthrough retains Persistent Labs as the host identity, with Alfred branding scoped to Alfred’s name and product sections. Instinct is an external inspiration and market benchmark; its financing and adoption figures are not Alfred traction. Bank-native, co-brand, white-label and bank-controlled deployment are proposed routes to validate, not claims of existing Alfred bank readiness.


### Typography and spacing · v0.2

Four review passes expanded the brand skill into a reproducible type and spacing contract:12 complete type roles, bundled font-loading CSS, a4px spacing scale, semantic layout gaps, card/control recipes, narrow-card action stacking, responsive media boundaries and an optional shadcn/Tailwind v4 integration fragment.

- [Typography and spacing specimen](https://nonprophet-max.github.io/alfred-walkthrough/skills/alfred-brand/assets/examples/type-spacing.html)
- [Exact font/spacing contract](skills/alfred-brand/references/typography-and-spacing.md)
- [shadcn integration](skills/alfred-brand/references/shadcn-integration.md)
- [Four-pass review record](skills/alfred-brand/references/design-review-2026-10-30.md)

From the repository root, run `python3 skills/alfred-brand/scripts/check_contract.py`. After deliberate token edits, run `python3 skills/alfred-brand/scripts/build_tokens.py` first. The helpers use only Python’s standard library. Browser verification covered320px,390px,768px and1440px, loaded fonts, computed typography, spacing, touch targets, keyboard focus, long labels and200% text size. No React/shadcn application was installed or compiled; the bridge is a reviewed integration reference. The older v0.1 ZIP remains available as an archive.
