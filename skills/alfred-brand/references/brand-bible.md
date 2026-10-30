# Alfred brand bible

**Provisional v0.2 · 30 October 2026**

This edition records the current owner-selected direction and the three-page Alfred pitch. It is a working identity, ready to use and refine; it does not establish trademark registration, a live product or bank approval.

## 1. Positioning

**Life, handled.**

Alfred is a proposed personal AI assistant for finding, booking and buying, starting in Telegram. It should become the place a person begins an everyday task—and the service that carries it through.

The initial scope is bookings, price search and sourcing, and executing retail purchases. An optional Alfred-branded prepaid/debit or card-linked experience could connect spending, rewards, benefits and follow-through. The exact programme remains to be integrated with appropriate partners.

The ambition spans a standalone consumer product and bank/neobank distribution. A bank may offer Alfred, co-brand it, or use its own identity on a native or white-label experience. A bank-controlled/on-prem route is an architectural ambition to validate.

**Instinct is the external inspiration and market benchmark. Alfred is our proposed product. FireFlow is the proposed foundation.** Instinct’s adoption signals and funding support the category thesis; they are never Alfred’s traction. Avoid presenting a third-party product demonstration as an Alfred demonstration.

### The architectural story

FireFlow offers a starting foundation for durable workflows, permission boundaries, approval pauses, isolated execution, recorded events and recovery. This foundation of reliability lets Alfred both serve **you** effectively from your pocket via Telegram or be deployed as a scaled, personalised Chief of Staff utility for the user base of an entire digital banking app.

A conversational interface alone does not supply banking-grade execution controls. Explain that architectural gap precisely; do not claim that every other assistant lacks such controls, or that using FireFlow automatically makes Alfred compliant or bank-ready.

## 2. Visual character

**Bold type. Quiet palette. A little personality.**

The owner’s preferred reference combined enormous black typography, outlined rounded frames, a tactile print feel and comic illustration. Alfred keeps those cues while reducing colour to isolated pink and blue flourishes.

Use a mostly black-and-white composition with strong hierarchy and readable space. The graphic idea should explain something: handing off a task, approving an action, connecting a card, or recovering work. A large headline and one memorable image usually do more than a dashboard of boxes.

The earlier yellow, sage and multicolour design previews were explorations. They do not define this edition.

## 3. Colour

| Token | Value | Role |
| --- | --- | --- |
| Ink | `#111110` | Display type, body text, outlines, dark fields |
| Paper | `#F7F7F2` | Main reading and presentation surface |
| White | `#FFFFFF` | Clean component surfaces and reversed text |
| Muted ink | `#353530` | Secondary text on light surfaces |
| Pink | `#FF4FA0` | Small emphasis, a clear action, a key detail |
| Blue | `#1975FF` | Small channel/category cues, a card corner or graphic mark |

Neutral fields dominate. Around 90% neutral is a useful composition target, not a pixel quota. Give each accent a job. A small pink approval button, blue card corner or isolated star can carry the identity; full-page pink/blue washes are outside the current direction.

Use ink labels on pink. For blue, choose a text pair that passes at the actual size: white on this blue is suitable for large text, not automatically for small body copy. Do not use a blue tint as faint reading text. The package includes calculated pair ratios in `assets/contrast.json`.

## 4. Typography

| Role | Typeface | Guidance |
| --- | --- | --- |
| Wordmark and display | Archivo Black | Supplied regular weight 400; the face itself is heavy |
| Body and interface | Space Grotesk | Regular/medium body; stronger weights for labels and emphasis |
| Metadata and folios | JetBrains Mono | Short uppercase labels, page numbers, amounts when useful |

Use supplied font files rather than relying on a remote font service. Never synthesize a heavier Archivo Black. Tight display spacing is appropriate, but letters must remain distinct.

On a 1920 × 1080 slide, the current system uses roughly 95–198 px display type, 24–38 px body copy and 18–22 px labels. These are examples from the pitch, not a requirement to force every artifact into that format. For reading websites, use comfortable 16–20 px body text and responsive layout.

The exact implementation contract is now in [Typography and spacing](typography-and-spacing.md). It specifies every role’s family, weight, size, line-height and tracking. Product body text is Space Grotesk 400 at 16/24px; component titles use Space Grotesk 600 at 20/28px. Large editorial headings use Archivo Black 400. Labels and instructions must remain readable rather than being scaled with an entire slide on a phone.

The supplied fonts.css loads the actual bundled faces. Use the generated type-role classes and verify loaded fonts in the browser; a family name in CSS does not establish that the intended file rendered.

## 5. Wordmark and avatar

The wordmark is lowercase **alfred**, set from Archivo Black with the spacing used in the current pitch. Use the supplied outlined SVGs; they do not depend on installed fonts.

Keep the wordmark in ink on light backgrounds or white on ink. A working clear-space allowance is half the visible wordmark height on each side. Keep it legible at small sizes; use the circular `a` avatar when the full name will not fit.

Preserve proportions. Do not add a new emblem, bevel, chrome effect or gradient. Do not imply a registered mark. The wordmark may sit on a tilted card, but its own geometry remains intact.

## 6. Illustration and the little concierge

The current signature illustration is a black bow tie with white gloves and shoes, carrying a hotel key, travel ticket, shopping bag and payment card. It communicates capable everyday assistance without becoming a generic robot.

Use the supplied transparent PNG. Its small pink key tag and blue card detail are intentional. Black contours, stippling and cross-hatching carry the print texture. Keep the silhouette clear and the illustration large enough to read.

In a long walkthrough, use the character at an Alfred introduction and selected product moments. Avoid repeating the full figure beside every paragraph. A compact avatar or wordmark can identify smaller mentions.

For a new illustration, retain thick expressive black ink, white/paper fills, sparse pink/blue details and a relevant everyday task. Generate original artwork; do not reproduce the supplied inspiration image’s skeletons, car or layout. Avoid generic glowing AI orbs, soft 3D renders and unrelated decoration.

## 7. Composition and components

Rounded black frames, outlined pills and confident dividers are part of Alfred. On the current slide canvas, internal outlines are about 3 px, the outer frame 5 px, and hard shadows about 4–9 px. Scale those relationships to the medium rather than copying slide measurements into every web button.

Use hard offset shadows selectively. Texture is subtle and should not reduce contrast. The PDF can omit page-wide grain to stay compact while retaining ink texture in the illustration.

Use the 4px spacing scale and semantic gaps from the typography/spacing contract. Related content uses 16px; card/form groups 24px; labels and controls 8px; actions 12px. Card padding is 20px on phones and 24px wider. Default controls have a 44px minimum target and 16px text. One layout owner sets each gap, preventing doubled card/slot padding.

For the online pitch, preserve one dominant idea per page and the approved vertical phone layout through 1000px. Desktop, PDF and embedded slide exports retain the authored 16:9 composition. Bottom navigation stays visible; content must have enough reserved space to scroll above it. The old whole-slide scaling rule applies to exports, not to phone reading.

[shadcn integration](shadcn-integration.md) explains semantic theme mapping, shared component recipes, font variables and portal isolation. Alfred’s fonts and geometry take precedence over generic starter defaults.

## 8. Product and card concepts

Telegram is Alfred’s proposed first native experience: conversation, useful choices, approval and task follow-through. It is not a claim that Telegram contains no competing assistants.

Show the customer’s request, meaningful options, approval before the illustrated purchase, and the result. A confirmation should say what happened; it should not substitute confidence for evidence.

The optional card is shown in ink with a small blue corner, the white Alfred wordmark and a pink detail. It represents a future branded spending/rewards relationship. Do not add network or issuer logos, real card credentials, promised reward rates or live-account claims without an actual authorized programme.

## 9. Voice

Write like a capable, friendly concierge: direct, warm, calm and lightly playful. State the useful outcome first. Use familiar verbs and concrete actions.

| Context | Example |
| --- | --- |
| Brand promise | “Life, handled.” |
| Functional promise | “Find it. Book it. Buy it.” |
| Invitation | “Your next move starts with a message.” |
| Product example | “I compared price, stock and delivery. Here’s the best match.” |
| Approval example | “Approve €229” |
| Completion example | “Ordered. Receipt and tracking saved.” |
| Recovery example | “The booking wasn’t confirmed. I’ll show you the next option.” |

Product examples describe an illustrative future experience unless live functionality has been established. Avoid inflated AI language, invented savings or claims that Alfred can do everything. Keep humour away from money, consent, failures and sensitive decisions.

## 10. Claims and market proof

Attribute Instinct’s funding and adoption figures to Instinct and the dated source. Label company-reported engagement separately from independently measured scale. Keep transaction volume, revenue, financing and valuation distinct.

Alfred’s intended differentiation is the combination of a Telegram-native service, everyday task execution, a card/benefits relationship and a FireFlow-based route into bank environments. “Better” is the product ambition; prove it with task completion, retention, safety, recovery and cost evidence.

Do not invent issuer agreements, bank clients, revenue, deployment certifications, absolute security, exactly-once external purchases or universal spending ceilings. Use a concise proposal label where it matters, rather than burying the story in repeated disclaimers.

## 11. Mixed-brand documents

In the full research walkthrough, **Persistent Labs remains the host brand**: its logo, navigation, Red Hat typography, graphite/gold surfaces and research/evidence style stay intact.

Apply Alfred’s identity locally to Alfred’s name and product material: the outlined wordmark or display face, monochrome product panels, isolated pink/blue accents, its card concept and the little concierge. Keep functional controls readable. Scope token overrides to Alfred components rather than changing the entire host document.

Instinct remains an external case study. Use explicit labels such as “External inspiration” and “Market benchmark”; do not put its name in an Alfred product lockup. Keep FireFlow’s own technical surface distinct. Alfred’s use of FireFlow is the proposed architecture, not an assertion of a new portfolio affiliation or signed partnership.

## 12. Implementation specimens and verification

Use [the live typography and spacing specimen](../assets/examples/type-spacing.html) to see the role hierarchy, spacing ladder and a realistic approval card. It includes both ordinary and long-label cases and a host/inset example. It is a plain-CSS reference; it does not claim that shadcn is installed or compiled here.

The package includes a repeatable contract check for role completeness, font files, generated CSS and portable references. Browser checks additionally inspect loaded fonts, computed type, actual spacing, touch targets, focus, text enlargement and horizontal overflow. The [four-pass review record](design-review-2026-10-30.md) records the baseline gaps, reviewed shadcn material, decisions and verification boundaries.

## 13. Assets, usage and status

Use [the asset map](assets.md) to find outlined wordmarks, the avatar, illustration, card concept, typefaces and tokens. The package is portable: preserve the folder structure when installing or sharing the skill.

To use without installation, ask an agent to read `skills/alfred-brand/SKILL.md` in the repository and follow its relative references. To install, place the downloaded `alfred-brand` folder in your agent’s skills directory, then invoke `$alfred-brand` in an environment that supports it. Automatic discovery remains enabled by default.

The brand bible and skill do not authorize publication or account changes. Apply the owner’s current brief over this provisional edition. When the identity changes, update the canonical bible and tokens together and regenerate the human-readable page and download.
