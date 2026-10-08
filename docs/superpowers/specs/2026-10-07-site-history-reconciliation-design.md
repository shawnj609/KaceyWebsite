# Site History Reconciliation Design

## Goal

Rebuild the intended current website from the published September 29 `main` commit while recovering approved local-only work, without reintroducing stale page structures or losing the standalone Fire page.

## Authoritative Baseline

Commit `446135c` (`Complete portfolio media galleries`) is the reconciliation base because it is the latest commit on GitHub `main`, deployed successfully to GitHub Pages, and contains the current production architecture.

The reconciliation must preserve from that baseline:

- The standalone `fire.html` page and its inclusion in the Pages workflow.
- The Earth / Air / Fire / See elemental navigation on every page.
- The current home page copy and layout.
- The published About page headed `See What's Next` with its Instagram call to action.
- The Nebula gallery on `mother-of-drones.html`, not on the About page.
- The Hekate's Torch content, sponsorship deck, and gallery on `fire.html`, not on the Mother of Drones page.
- The September 29 Blood Sisters episode gallery, filmmaker sections, Lone Star Swing links, voiceover section, responsive rules, and production assets.

## Recovered Changes

### Mother of Drones

The hero credit will read `Painting The Sky With Light`.

The Design Work gallery will use the same card sizing and responsive layout as the actor Reel Gallery. It will remove the obsolete drone-only portrait fallback classes while retaining the existing modal behavior.

The gallery will contain these 16 videos in this exact order:

1. `CrQbV0Hd5n0` — Necker Island Show vs Render
2. `J-3Gb_1-C48` — 2023 Necker Island New Years Show Render
3. `h5r-xJK7PQU` — Chinese New Year Render and Show - Stacked
4. `wPpaF_1U5SU` — Flipside 25 Effigy Render
5. `g6U8P0PHcb4` — FreezerBurn 26 Duck Suff III Render
6. `Izd_hZuCFCk` — Four Seasons render
7. `BOw-psHSoF0` — Viking Ship Funeral Fire Render
8. `IFW1qV5zMw8` — 2023 Necker Island New Years Drone Show
9. `dx6Sr3N3Gzk` — 2023 Burning Man Drone Design Collab with Zeplin
10. `n6sXgD5Go80` — Banksey Girl With The Red Balloon Drone Render
11. `1oMTPBuUZSo` — 2025 ABQ Balloon Fiesta Render
12. `TfgDetMAd5s` — Drone Design for Chinese New Year and Marina Bay Sands
13. `IOym9A9l5Pw` — 2023 4th Drone Design at the Sphere
14. `vWwH7TSeENI` — Chinese New Year Render
15. `dgYVwMrPL1k` — Chinese New Year Render And Show
16. `3YX8aV7nboI` — BigAss Render

Each card will use its direct YouTube link, YouTube thumbnail, descriptive visible title, matching alternative text, and accessible label.

### Actor and Filmmaker

The hero credit order will read `Film · TV · Stage`.

The eleven existing acting reel cards will keep their current order, links, thumbnails, modal behavior, and layout while replacing generic reel numbers with these approved titles:

1. Project Rant
2. Chumps
3. Trojan
4. Kleenex
5. Grande
6. Nike
7. What's Your Emergency?
8. Barton Underwater
9. Amazon Underwater
10. Undo Part One
11. Undo Part Two

Each reel image alternative text will use its corresponding approved title.

The Voiceover gallery will add `Fef8IC-1ktg` — `Talk Dirty To Me Intro` as its first card while preserving the three published demos and their order.

The published `Actress & Filmmaker` heading and Earth / Actress navigation wording remain unchanged. The direct-label navigation found in the stale working tree will not be restored because it removes the elemental navigation and the standalone Fire page.

## Excluded Stale Changes

The following dirty-working-tree changes will not be carried into production:

- Deleting `fire.html` or removing it from the Pages workflow.
- Moving Hekate's Torch into the Mother of Drones page.
- Moving Nebula from Mother of Drones to About.
- Replacing the published About page with the older `Who Is She?` placeholder version.
- Replacing elemental navigation with direct Actor / Drone Artist / About labels.
- Deleting published assets such as `assets/kacey.webp`, `assets/oh-my.png`, or the tracked drone media.
- Adding the unreferenced raw `.mov` staging files to production.
- Replacing newer published CSS wholesale with the older local stylesheet.

The original dirty checkout will remain untouched during reconciliation so it continues to serve as a recovery source.

## Implementation Approach

Work will continue in an isolated branch created directly from `origin/main`. The already-tested drone header and gallery changes will be reapplied from the local feature branch, then extended to 16 videos. Actor titles and the additional voiceover card will be implemented narrowly on top of the production actor page.

Only `actor.html`, `mother-of-drones.html`, `site.css`, and focused regression tests should need content changes. Stylesheet cache keys on affected pages will be advanced so Safari and other browsers request the reconciled stylesheet immediately.

## Verification

- Add or update regression tests for the exact 16-video drone order, titles, links, thumbnails, alternative text, and labels.
- Verify the Mother of Drones hero credit and shared Reel Gallery layout.
- Add regression coverage for the exact actor reel title mapping and `Film · TV · Stage` credit order.
- Verify `Talk Dirty To Me Intro` precedes the three existing voiceover cards.
- Assert `fire.html` exists, every page retains its Fire navigation link, and the deployment workflow copies `fire.html`.
- Assert Nebula remains on Mother of Drones and Hekate's Torch remains on Fire.
- Run the complete static test suite.
- Start the local server and inspect desktop and mobile layouts, links, navigation, and representative video modals.
- Show the localhost preview to Kacey for approval.
- Do not push to `main` until Kacey approves the preview and explicitly authorizes the push.
