# Kacey Samiee Website

Static starter site for `kaceysamiee.com`, owned under the active GitHub account `shawnj609`.

This repo intentionally follows the simple production pattern from `shawnj609/NebulaWebsiteV2`: plain HTML, plain CSS, a `CNAME`, a `.nojekyll` marker, and a GitHub Pages Actions workflow. There is no Node, package manager, build framework, CMS, database, or separate hosting runtime.

## Current Site Files

- `index.html` - the public starter page.
- `site.css` - all styling for the starter page.
- `assets/kacey.webp` - starter portrait asset sourced from the Nebula website assets.
- `CNAME` - custom domain for GitHub Pages: `kaceysamiee.com`.
- `.github/workflows/deploy-pages.yml` - deploys to GitHub Pages on every push to `main`.
- `docs/HOSTING_AND_EDITING.md` - deployment, Bluehost DNS, and editing notes for future agents.
- `AGENTS.md` - guardrails for Codex or other agents working in this repo.

## Run Locally

From the repo root:

```bash
python -m http.server 8080
```

Then open:

- `http://localhost:8080/index.html`

Opening `index.html` directly in a browser also works because the site has no build step.

## Deploy

Push to `main`:

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

