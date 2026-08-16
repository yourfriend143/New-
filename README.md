# Saini TXT Leech Bot — Koyeb

Telegram bot for processing video/text links and related downloads.

## Koyeb deployment

Deploy this repository as a **WORKER** service using the repository `Dockerfile`.
Do not expose an HTTP port; the bot runs as a long-lived Telegram worker.

### Required environment variables

- `API_ID` — Telegram API ID
- `API_HASH` — Telegram API hash
- `BOT_TOKEN` — Telegram bot token
- `OWNER` — Telegram numeric user ID of the owner

### Optional environment variables

- `CREDIT`
- `AUTH_USERS` — comma-separated Telegram user IDs
- `TOTAL_USERS` — comma-separated Telegram user IDs
- `cookies_file_path` — defaults to `youtube_cookies.txt`
- `API_URL` — defaults to `http://master-api-v3.vercel.app/`
- `API_TOKEN` — token for the external DRM/master API, if required by the bot

Keep all credentials in Koyeb environment variables/secrets. Do not commit them to GitHub.

## Koyeb settings

- Service type: **Worker**
- Builder: **Dockerfile**
- Dockerfile path: `Dockerfile`
- Command: leave the Dockerfile command unchanged
- Port: none
- Minimum instances: 1

The Docker image installs FFmpeg, aria2 and Bento4 (`mp4decrypt`) and then starts `modules/main.py`.
