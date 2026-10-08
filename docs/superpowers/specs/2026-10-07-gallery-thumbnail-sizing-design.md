# Gallery Thumbnail Sizing Design

## Goal

Make the thumbnails in Actor Reels, Design Work, and Hekate's Gallery match the established Blood Sisters thumbnail size and responsive behavior.

## Reference Pattern

Blood Sisters is the visual and structural reference. Its thumbnails use:

- A full-width gallery region.
- Three equal columns on desktop.
- The shared `16 / 10` thumbnail aspect ratio.
- The existing shared gallery gap.
- One column on mobile.

At the current 934px preview width, Blood Sisters cards render at approximately 276 by 173 pixels. The target galleries must render at the same dimensions, subject to normal rounding.

## Layout

Actor Reels, Design Work, and Hekate's Gallery will use the same full-width grid geometry as Blood Sisters. Their section headings will move above the grids because a side-by-side heading column leaves insufficient width for Blood Sisters-sized cards.

The change is limited to layout. Existing card artwork, titles, links, play controls, colors, animation, and section order remain unchanged.

## Responsive Behavior

- Desktop: three equal columns matching Blood Sisters.
- Mobile at the site's existing gallery breakpoint: one full-width column matching Blood Sisters.
- Section headings remain readable above their grids at every supported width.
- No horizontal overflow is introduced.

## Verification

- Add a regression check that confirms the three target galleries share Blood Sisters' desktop grid geometry and mobile column behavior.
- At the 934px preview width, compare rendered card dimensions and confirm the target cards match Blood Sisters within one pixel.
- Inspect Actor Reels, Design Work, and Hekate's Gallery on desktop and mobile.
- Confirm links, video modal behavior, captions, and navigation still work.

## Out of Scope

- Changing the Photo Reel, Voiceover, Nebula, or filmmaker-project galleries.
- Reordering or replacing gallery content.
- Changing thumbnail cropping, typography, colors, or motion.
