# Kacey Samiee Website

Static starter site for `kaceysamiee.com`, owned under the active GitHub account `shawnj609`.

This repo intentionally follows the simple production pattern from `shawnj609/NebulaWebsiteV2`: plain HTML, plain CSS, a `CNAME`, a `.nojekyll` marker, and a GitHub Pages Actions workflow. There is no Node, package manager, build framework, CMS, database, or separate hosting runtime.

## Current Site Files

- `index.html` - the public starter page.
- `site.css` - all styling for the starter page.
- `assets/fonts/` - the three self-hosted typefaces. Bodoni Moda for display, Archivo for body copy, Fragment Mono for navigation, buttons, and captions. All three are SIL Open Font License and total about 96 KB.
- `assets/kacey.webp` - starter portrait asset sourced from the Nebula website assets.
- `CNAME` - custom domain for GitHub Pages: `kaceysamiee.com`.
- `.github/workflows/deploy-pages.yml` - deploys to GitHub Pages on every push to `main`.
- `docs/HOSTING_AND_EDITING.md` - deployment, Bluehost DNS, and editing notes for future agents.
- `AGENTS.md` - guardrails for Codex or other agents working in this repo.

## Run Locally

Start the server from the repo root, the folder that contains `index.html`, `site.css`, and `assets/`:

```powershell
cd C:\Users\shawn\Code\Repos\KaceyWEbsite\KaceyWebsite
python -m http.server 8080
```

Then open:

- `http://localhost:8080/`
- `http://localhost:8080/index.html`

Do not use `http://localhost:8080/index`; Python's static server does not map that path to `index.html`.

If `8080` is already in use, stop the stale server or run on another port:

```powershell
python -m http.server 8081
```

Opening `index.html` directly in a browser also works because the site has no build step.

## Agent Preview Flow

When Kacey asks for site changes, show the edited site on localhost first and ask her to approve that preview. After she approves the local version, ask whether she wants the change pushed to `main`; pushing to `main` is what publishes the change to the real GitHub Pages site.

## Deploy

After local preview approval, push to `main`:

```bash
git push origin main
```

GitHub Actions runs `Deploy GitHub Pages`, creates a static `_site` bundle, uploads it as a Pages artifact, and deploys it to GitHub Pages.

## Hosting Notes

- GitHub Pages should use `GitHub Actions` as the build and deployment source.
- The custom domain is `kaceysamiee.com`.
- DNS is expected to be managed at Bluehost because that is where the domain is already hosted.
- The GitHub Pages DNS records and Bluehost edit path are documented in `docs/HOSTING_AND_EDITING.md`.

## Future Edit Rules

- Keep the site static until Kacey asks for functionality that proves a framework is needed.
- Keep production images optimized as `.webp`.
- Do not reference files from `photo_inbox/` in production HTML.
- If deployment, domain, or workflow behavior changes, update `README.md`, `AGENTS.md`, and `docs/HOSTING_AND_EDITING.md` in the same change.

