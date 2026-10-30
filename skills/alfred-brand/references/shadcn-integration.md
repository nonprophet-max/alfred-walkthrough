# Alfred with shadcn/ui

Use this only when the target project actually uses shadcn. The brand kit itself is plain HTML/CSS; reviewing shadcn does not require installing React, changing a preset, running init or installing every component.

## Establish the target

Read its components.json and package manager. Use the installed shadcn skill/CLI to inspect `info --json`, actual component source and current docs before changing components. Confirm Tailwind version, base library, aliases, style and resolved CSS path. Preserve existing component APIs, accessibility and variants. Do not switch a preset or import path from memory.

## Theme and font wiring

For a **standalone Alfred app**, copy the font files and import `fonts.css` and `tokens.css` in the existing global CSS. The supplied `assets/shadcn-v4.css` is a Tailwind v4 integration fragment, not a complete app and not suitable for pasting into Tailwind v3. It registers Alfred families and type-* utilities and maps semantic colours under `.alfred-theme`.

Apply `alfred-theme alfred-surface` at the standalone app root. Existing shadcn components use semantic colours such as bg-background, text-foreground and bg-primary. Map button `default` to pink/ink; keep ordinary surfaces paper/ink and card interiors white/ink. Blue is a restrained graphic/focus accent, not a small white-text button. Keep any existing destructive/status roles until they are specifically designed and contrast-checked; do not invent financial states from decorative colours.

Use Space Grotesk for `font-sans` and `font-heading`, JetBrains Mono for `font-mono`, Archivo Black for `font-display` and large display roles. Literal family names plus the supplied @font-face declarations provide a simple reliable route. Do not retain Geist because it was the starter preset’s font. Do not generate `--font-sans: var(--font-sans)`.

If the project uses next/font, apply its generated font variables at the correct root and wire @theme inline to those distinct variables. Tailwind explicitly supports this form. The blanket claim that runtime font variables can never work is incorrect; missing scope and self-reference must be diagnosed by inspecting the actual output. Do not mix a bundled @font-face route and next/font for the same family without a reason.

The generated type-* utilities set family, size, weight, leading and tracking together. Place them in shared component definitions/variants; keep call-site className for layout. Distinct type-* names avoid a typography role being confused with a text-colour utility by class-merging tools. Verify the project’s actual cn()/tailwind-merge behaviour rather than assuming a class string proves it.

## Geometry lives in shared recipes

Inspect built-in Card spacing and control sizes. Modify shared component bases/cva variants, preserving existing variant names. Pin Button, Input, Select, Textarea and relevant triggers to Alfred’s typography and 44px minimum targets together. A larger Button beside an unchanged 32px Input is not a coherent system.

- Card root: 20px phone / 24px wider padding, 24px group gap, 2px border, 20px radius. CardHeader/CardContent/CardFooter have zero padding in this recipe; header title-to-description gap is 8px. Set container-type:inline-size and container-name:alfred-card on the root so actions respond to available card width.
- CardTitle/DialogTitle: component-title = Space Grotesk 600, 20/28px, −0.015em. Archivo Black is reserved for larger editorial headings.
- Forms: FieldGroup + Field, with the semantic 24px group and 8px label/control/help spacing. Keep field labels and validation semantics. Error/help copy uses body-small, not a tiny caption.
- Button default/outline: control role, 44px minimum, 8/12px padding, 12px radius. Default uses pink/ink and an optional hard shadow. Icon targets are at least size-11. Use built-in icons via data-icon as the installed component expects.
- Sibling layout uses flex/grid gap; choose one density. Use cn() and existing variants; do not scatter font, colour and padding overrides across every usage.

A composition after the shared recipes have been applied:

```tsx
// Imports use the target project's actual aliases; shown with @/ as an example.
import { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter } from "@/components/ui/card"
import { Button } from "@/components/ui/button"

export function PurchaseApproval() {
  return (
    <Card>
      <CardHeader>
        <CardTitle>Ready when you are.</CardTitle>
        <CardDescription>Headphones, delivered by Friday.</CardDescription>
      </CardHeader>
      <CardContent>
        <p className="type-amount">€229 delivered</p>
      </CardContent>
      <CardFooter className="alfred-actions">
        <Button className="w-full flex-1">Approve €229</Button>
        <Button variant="outline" className="w-full flex-1">Review details</Button>
      </CardFooter>
    </Card>
  )
}
```

This is an integration recipe, not a claim that a shadcn runtime is bundled or compiled in this repository. The executable browser specimen uses the equivalent generated plain CSS.

## Portals and host isolation

For an Alfred inset inside Persistent Labs, use the prefixed plain CSS and local component recipes. Global font-sans/radius overrides would change the host. For portalled menus, dialogs and sheets, supply a themed portal container or the theme/surface classes on the portal content itself so font and semantic variables do not disappear outside the wrapper. Preserve accessible titles, focus management, Escape, keyboard order and validation. Do not add manual z-index values to library overlays to compensate for a broken theme.

## Relevant sources checked 30 October 2026

- [shadcn theming](https://ui.shadcn.com/docs/theming): semantic surface/foreground roles.
- [shadcn Typeset](https://ui.shadcn.com/docs/typeset): current typography tooling destination.
- [shadcn Card](https://ui.shadcn.com/docs/components/card): component slots and composition.
- [Tailwind theme variables](https://tailwindcss.com/docs/theme#referencing-other-variables): @theme inline and referenced variables.
- [Tailwind font-family](https://tailwindcss.com/docs/font-family) and [gap](https://tailwindcss.com/docs/gap): utility wiring.

The numeric Alfred type and spacing values are our brand decisions, not values prescribed by those sources. Local shadcn skills were also reviewed for styling, customization, design-system mapping, shared control sizes and visual specimens. Their generic font, dark-mode and compact-density defaults do not override Alfred.
