# Agent Instructions

This repository is a small static GitHub Pages website for `kaceysamiee.com`.

## Intentional Architecture

- Plain HTML and CSS only.
- Primary branch: `main`.
- Deployment: GitHub Pages through `.github/workflows/deploy-pages.yml`.
- Custom domain: `kaceysamiee.com` through `CNAME`.
- Hosting DNS: Bluehost DNS records pointing to GitHub Pages.

Do not introduce Next.js, Vite, React, Tailwind, Supabase, a CMS, or a package manager unless Kacey or Shawn explicitly asks for a feature that needs it.

## Deployment Source

This repo is patterned after `shawnj609/NebulaWebsiteV2`, which deploys a static HTML/CSS site to GitHub Pages with a custom GitHub Actions workflow. Kacey's repo keeps that model but uses `main` instead of Nebula's `master` branch.

## Editing Guidance

- Edit `index.html` for content and structure.
- Edit `site.css` for styling.
- Put final production assets in `assets/`.
- Use `.webp` for photos and other raster production images.
- Use `photo_inbox/` only for raw or temporary photo staging; it is ignored by git and must not be referenced by production HTML.
- Keep the workflow bundle list in sync when adding production files or folders.
- Preserve `CNAME` unless the canonical domain changes.

## Verification

Before committing meaningful changes:

1. Run a local static server with `python -m http.server 8080`.
2. Check `http://localhost:8080/index.html` on desktop and mobile width.
3. Confirm image paths, navigation anchors, and responsive layout work.
4. Push to `main` and check the GitHub Actions Pages deployment.

## Documentation Updates

If you change hosting, DNS assumptions, branch names, deploy workflow behavior, or asset policy, update:

- `README.md`
- `docs/HOSTING_AND_EDITING.md`
- this `AGENTS.md`

