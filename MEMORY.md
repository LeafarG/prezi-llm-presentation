# llm-presentation — Project Memory

**One-liner:** Static single-file HTML presentation on LLM history, types, ecosystem (PT-BR). Two Vercel projects (v1 + Prezi variant), both auto-deploy on push via Vercel GitHub App.

## Live

- **v1 (original):** https://llm-presentation-beta.vercel.app — repo `LeafarG/llm-presentation`, branch `main`, Vercel project `prj_vV0D5XkYCUIaNcjvV3Vjl8plmpvJ`
- **Prezi variant:** https://prezi-llm-presentation.vercel.app — repo `LeafarG/prezi-llm-presentation` (standalone, NOT a GitHub fork), branch `main` ← was `feat/prezi-style` in the v1 repo before being mirrored, Vercel project `prj_afadzrtQg2OjZPktLH3S1SiPt0jd`
- **Team scope:** `leafargs-projects` (`team_eXXOxECFjvUEbTXratuOKotI`)

## Local remotes (in `D:\.openclaw\workspace\projects\llm-presentation`)

- `origin` → `LeafarG/llm-presentation` (v1)
- `prezi` → `LeafarG/prezi-llm-presentation` (Prezi variant)
- Current branch: `feat/prezi-style` — the local branch name is unchanged because both repos track the same code; push to either remote's `main`.

## Stack

- Pure static: one `index.html` with inline CSS + JS, no build, no deps
- Framework preset on Vercel: "Other" (auto-detected)
- Node version: 24.x

## Deploy

Auto-deploy via Vercel GitHub App on push to `main`. Initial link done 2026-07-07 via `POST /v9/projects/{id}/link` after boss installed the Vercel GitHub App on LeafarG org. See `D:\.openclaw\workspace\MEMORY.md` 2026-07-07 entry for full link-API pattern.

For manual deploy (rare):
```bash
vercel --prod
```

## Project layout

```
projects/llm-presentation/
├── .vercel/project.json     # local-only (gitignored since 2026-07-07)
├── .gitignore               # .vercel/, node_modules/, editor cruft
├── index.html               # the whole site (HTML+CSS+JS)
├── README.md                # deployment notes
└── SPEC.md                  # original content spec
```

## Critical config

- **No env vars** — pure static, nothing to configure.
- **Vercel CLI 54.14.0** at `C:\Users\rafae\AppData\Roaming\npm\vercel.ps1` — call via the underlying `node ...\vc.js` to avoid the npm shim's stderr pollution (per chat-with-history / rafaelgomes-landingpage precedents).
- **GitHub CLI** at `C:\Program Files\GitHub CLI\gh.exe`; PAT cached as `GH_TOKEN` only when needed (gho_… token has `gist, repo, workflow` scopes).

## Notable gotchas

- **No `.gitignore` originally** — committed `.vercel/project.json` was a non-issue (Vercel-internal), but I added a proper `.gitignore` on 2026-07-07 to prevent future contributors from accidentally committing `.vercel/` updates or editor config.
- **Vercel deployment READY but the `latestDeployments` array on GET /v9/projects/{id} showed `[…]` (empty)** initially right after linking — the first push populated it. Don't panic if it lags for ~10 s post-push.
- **Auto-deploy link via API required Vercel GitHub App installed first** — see MEMORY.md. Don't waste cycles on the token-creation path (`/v3/user/tokens` rejects OAuth CLI tokens with "Cannot create tokens for this app").
- **GitHub blocks forks under the same owner account** — `POST /repos/{owner}/{repo}/forks` returns `cannot be forked. A single user account cannot own both a parent and fork` when both repos would belong to the same user. The `LeafarG/prezi-llm-presentation` repo was therefore created as a **standalone repo** rather than a fork. It mirrors the v1 content but lacks the GitHub fork-badge link. Functionally identical for Vercel auto-deploy.
- **Project creation via `vercel api /v10/projects -X POST --input NAME.json` works fine**, but the **link endpoint (`/v9/projects/{id}/link`) requires `-F KEY=VAL` form fields** — `--input FILE` returns `415 Unsupported Media Type`. The `/v9/projects/{id}/link` endpoint is undocumented (not in the public OpenAPI spec) but is the canonical link path for the Vercel GitHub App integration. Pattern verified twice (2026-07-07 v1 + Prezi).
- **SSO Protection is on by default for new Vercel projects** (`ssoProtection.deploymentType = "all_except_custom_domains"`). Disable for public previews: `vercel project protection disable <project> --sso --scope <team>`. Same gotcha as `rafaelgomes-landingpage` PR #9 (MEMORY 2026-06-30).

## Updates

- **2026-07-07**: Project shipped to prod (`vercel --prod`, no GitHub link). Per-chat-history pattern applied: SPEC → implementation → manual deploy.
- **2026-07-07 (later same day)**: Auto-deploy enabled via Vercel GitHub App. First auto-deploy commit `chore: enable auto-deploy via Vercel GitHub App` (`205d3ef`) verified end-to-end — push SHA matched deploy SHA within ~10 s.
- **2026-07-07 (afternoon, Prezi variant)**: Boss asked to "make this branch a fork". GitHub API blocks forks under same owner account, so `LeafarG/prezi-llm-presentation` was created as standalone repo (not a fork of `LeafarG/llm-presentation`). The `feat/prezi-style` branch was mirrored via `git push prezi feat/prezi-style:main`. A new Vercel project (`prj_afadzrtQg2OjZPktLH3S1SiPt0jd`) was created via `POST /v10/projects` and linked via `POST /v9/projects/{id}/link` with `-F` form fields (not `--input`). SSO disabled. Boss asked for the Vercel site to mirror the Prezi version while keeping the v1 site at the original URL — both auto-deploy from their respective GitHub repos now. Production: **https://prezi-llm-presentation.vercel.app**. Reverted one throwaway `chore(prezi): trigger Vercel auto-deploy` commit on first push (commit `25d482d`, reverted by `7f92abe`) to keep history clean.
