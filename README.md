# Game Hub

A static game site that runs on GitHub Pages. Everything is done in the browser on github.com.

## One-time setup

1. Sign in at github.com and click **New repository**. Name it anything (e.g. `games`), set it to **Public**, and create it.
2. Click **Add file → Upload files** and drag in `index.html`, `build_games.py`, `games.json`, and the `games` folder. Commit.
3. Click **Add file → Create new file**, type the name `.github/workflows/update-games.yml` (typing the slashes makes folders), paste in the workflow contents, and commit.
4. Go to **Settings → Actions → General → Workflow permissions**, choose **Read and write permissions**, and Save.
5. Go to **Settings → Pages**, set **Source** to *Deploy from a branch*, Branch **main**, folder **/ (root)**, and Save.
6. After a minute, your site is live at `https://YOUR-USERNAME.github.io/REPO-NAME/`.

## Adding a game

Put the game in the `games` folder using **Add file → Upload files**:

- **Folder game:** `games/my-game/index.html` (plus any other files the game needs: js, images, sounds). Upload the whole folder by dragging it in.
- **Single-file game:** `games/my-game.html`
- **Thumbnail (optional):** add `thumb.png` (or .jpg/.webp) inside the game's folder.
- **Custom title (optional):** add `game.json` inside the folder containing `{"title": "My Game"}`.

Commit the upload. A GitHub Action runs automatically (see the **Actions** tab), updates `games.json`, and the game shows up on your site about a minute later. If it doesn't appear, open **Actions → Update game list → Run workflow**.

## Notes

- Games must be HTML5/web games (HTML + JS). Flash or downloadable .exe games won't work.
- Games get stored as files in your repo, and GitHub's per-file limit is 100 MB (25 MB for browser uploads), so very large games may need to be uploaded in pieces.
- Hard refresh (Ctrl+Shift+R) if the list looks stale.
