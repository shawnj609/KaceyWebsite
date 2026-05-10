# Hosting And Editing Notes

Last checked: 2026-05-10.

This document exists so future agents keep Kacey's site on the same simple deployment path as Nebula instead of inventing a heavier stack.

## Source Pattern

The baseline is `shawnj609/NebulaWebsiteV2`, which is a static HTML/CSS repo deployed to GitHub Pages by Actions. The useful pieces copied forward are:

- Hand-authored HTML and CSS.
- `CNAME` for the custom domain.
- `.nojekyll` so GitHub Pages serves files directly.
- `.github/workflows/deploy-pages.yml` with `actions/configure-pages`, `actions/upload-pages-artifact`, and `actions/deploy-pages`.

Kacey's repo uses the same model with one deliberate difference: the deployment branch is `main`.

## Official References

- GitHub custom Pages workflows: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
- GitHub custom domain setup and DNS records: https://docs.github.com/articles/setting-up-your-pages-site-repository
- Bluehost DNS tab guide: https://www.bluehost.com/help/article/dm-guide-to-the-dns-tab-in-the-account-manager
- Nebula source repo: https://github.com/shawnj609/NebulaWebsiteV2

## Local Editing Flow

1. Edit `index.html`, `site.css`, and any files in `assets/`.
2. Run a local server from the repo root:

```bash
python -m http.server 8080
```

3. Open `http://localhost:8080/index.html`.
4. Verify layout at desktop and mobile widths.
5. Commit and push to `main`.

## Deploy Flow

The workflow runs on every push to `main` and can also be started manually from GitHub Actions.

The build job copies only production files into `_site`:

- `index.html`
- `site.css`
- `CNAME`
- `.nojekyll`
- `assets/`

The deploy job publishes that artifact to GitHub Pages.

If future work adds new production pages or folders, update the `Build static site bundle` step in `.github/workflows/deploy-pages.yml`.

## GitHub Pages Settings

In the GitHub repository:

1. Open `Settings`.
2. Open `Pages`.
3. Under `Build and deployment`, set `Source` to `GitHub Actions`.
4. Set the custom domain to `kaceysamiee.com`.
5. After DNS resolves, enable `Enforce HTTPS`.

The workflow includes `actions/configure-pages@v5` with `enablement: true`, matching the Nebula workflow pattern.
The other official Pages actions are kept on current Node 24-capable major versions where available.

## Bluehost DNS

Bluehost is expected to manage DNS for `kaceysamiee.com`.

In Bluehost:

1. Log in to the Bluehost Portal.
2. Open `Domains`.
3. Select `kaceysamiee.com`.
4. Open the `DNS` tab.
5. Use `Manage Advanced DNS Records`.

For the apex/root domain, add or update four `A` records:

| Type | Host | Value |
| --- | --- | --- |
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |

For `www`, add or update this record:

| Type | Host | Value |
| --- | --- | --- |
| CNAME | www | shawnj609.github.io |

DNS can take time to propagate. GitHub will not finish HTTPS certificate setup until the domain points correctly to GitHub Pages.

## Troubleshooting

- If the site deploys but the custom domain shows a GitHub 404, check `CNAME`, Pages custom domain settings, and Bluehost DNS records.
- If the workflow succeeds but a file is missing on the site, confirm the file is copied into `_site` in `.github/workflows/deploy-pages.yml`.
- If HTTPS cannot be enforced yet, wait for DNS propagation and re-check the Pages settings.
- If a future agent wants to add a framework, first prove why static HTML/CSS is insufficient.
