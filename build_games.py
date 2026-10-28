#!/usr/bin/env python3
"""Scans the games/ folder and writes games.json for the site.

Supported layouts:
  games/my-game/index.html        (folder game; optional thumb.png/jpg/webp/gif next to it)
  games/my-game.html              (single-file game)
Optional: games/my-game/game.json  ->  {"title": "My Game"}
"""
import json, os, re

GAMES_DIR = "games"
THUMB_NAMES = ["thumb", "thumbnail", "icon", "cover"]
THUMB_EXTS = ["png", "jpg", "jpeg", "webp", "gif"]


def pretty(name):
    name = re.sub(r"\.html?$", "", name, flags=re.I)
    return re.sub(r"[-_]+", " ", name).strip().title()


def slug(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


games = []
if os.path.isdir(GAMES_DIR):
    for entry in sorted(os.listdir(GAMES_DIR), key=str.lower):
        full = os.path.join(GAMES_DIR, entry)
        if entry.startswith("."):
            continue
        if os.path.isdir(full):
            if not os.path.isfile(os.path.join(full, "index.html")):
                continue
            title = pretty(entry)
            meta = os.path.join(full, "game.json")
            if os.path.isfile(meta):
                try:
                    title = json.load(open(meta, encoding="utf-8")).get("title", title)
                except Exception:
                    pass
            thumb = None
            for n in THUMB_NAMES:
                for e in THUMB_EXTS:
                    p = f"{n}.{e}"
                    if os.path.isfile(os.path.join(full, p)):
                        thumb = f"{GAMES_DIR}/{entry}/{p}"
                        break
                if thumb:
                    break
            games.append({"id": slug(entry), "title": title,
                          "path": f"{GAMES_DIR}/{entry}/index.html", "thumb": thumb})
        elif entry.lower().endswith((".html", ".htm")):
            games.append({"id": slug(entry), "title": pretty(entry),
                          "path": f"{GAMES_DIR}/{entry}", "thumb": None})

with open("games.json", "w", encoding="utf-8") as f:
    json.dump(games, f, indent=2)
print(f"Wrote games.json with {len(games)} game(s)")
