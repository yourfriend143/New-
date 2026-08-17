import os


def required_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


API_ID = int(required_env("23283708"))
API_HASH = required_env("7805011fb84729023531f0fa3f000bec")
BOT_TOKEN = required_env("8257275378:AAE3H-5tuILZPVxLXvcFothlT9sJRIzogFo")
OWNER = int(required_env("6481888008"))

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

# External DRM/master API configuration. Keep credentials in Koyeb Secrets/Env,
# never in GitHub source code.
api_url = os.getenv("API_URL", "http://master-api-v3.vercel.app/")
api_token = os.getenv("API_TOKEN", "")
