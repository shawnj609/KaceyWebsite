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
- Fonts are self-hosted in `assets/fonts/` and declared with `@font-face` at the top of `site.css`. Do not add a Google Fonts `<link>`; the site loads no third-party resources.
- Use `photo_inbox/` only for raw or temporary photo staging; it is ignored by git and must not be referenced by production HTML.
- Keep the workflow bundle list in sync when adding production files or folders.
- Preserve `CNAME` unless the canonical domain changes.

## Kacey Preview And Approval Flow

When Kacey asks for a change, make the local edits first and then show her the site on localhost before suggesting any push to production.

1. Start the local server from the repository root, the folder that contains `index.html`, `site.css`, and `assets/`:

```powershell
cd C:\Users\shawn\Code\Repos\KaceyWEbsite\KaceyWebsite
python -m http.server 8080
```

2. Open `http://localhost:8080/` or `http://localhost:8080/index.html`. Do not use `http://localhost:8080/index`; Python's static server does not map that path to `index.html`.

   Known limitation: `python -m http.server` answers `Range:` requests with `200` instead of `206`, so Chrome will not stream the background videos on the home and Mother of Drones pages. Those pages preview correctly except the video stays black. GitHub Pages supports Range, so this only affects local preview.
3. If port `8080` is already in use, either stop the stale local server or use the next clear port, such as `python -m http.server 8081`, and tell Kacey the exact localhost URL.
4. Ask Kacey to review the localhost version. Do not push to `main` until she approves the local preview.
5. After Kacey approves, ask whether she wants the change pushed to `main` so GitHub Pages can publish it to the real website.

## Verification

Before committing meaningful changes:

1. Run a local static server from the repository root with `python -m http.server 8080`.
2. Check `http://localhost:8080/` or `http://localhost:8080/index.html` on desktop and mobile width.
3. Confirm image paths, navigation anchors, and responsive layout work.
4. Get Kacey's approval on the localhost preview.
5. Push to `main` only after approval, then check the GitHub Actions Pages deployment.

## Documentation Updates

If you change hosting, DNS assumptions, branch names, deploy workflow behavior, or asset policy, update:

- `README.md`
- `docs/HOSTING_AND_EDITING.md`
- this `AGENTS.md`

