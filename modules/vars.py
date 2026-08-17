import os


def required_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


API_ID = int(required_env("API_ID"))
API_HASH = required_env("API_HASH")
BOT_TOKEN = required_env("BOT_TOKEN")
OWNER = int(required_env("OWNER_ID"))

CREDIT = os.getenv("CREDIT", "𝐑𝐒 𝐁𝐡𝐚𝐫𝐝𝐰𝐚𝐣")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")


def parse_user_ids(name: str, default: str = ""):
    raw = os.getenv(name, default).strip()
    if not raw:
        return []
    result = []
    for value in raw.split(","):
        value = value.strip()
        if value:
            result.append(int(value))
    return result


TOTAL_USERS = parse_user_ids("TOTAL_USERS")
AUTH_USERS = parse_user_ids("AUTH_USERS")
if OWNER not in AUTH_USERS:
    AUTH_USERS.append(OWNER)

