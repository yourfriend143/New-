from vars import OWNER, CREDIT
import threading
import time
import requests
import os

processing_request = False
cancel_requested = False
caption = '/cc1'
endfilename = '/d'
thumb = '/d'
CR = f"{CREDIT}"

# ────────────────────────────────
# 🔹 STATIC TOKENS (UNCHANGED)
# ────────────────────────────────
cwtoken = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3MjQyMzg3OTEsImNvbiI6eyJpc0FkbWluIjpmYWxzZSwiYXVzZXIiOiJVMFZ6TkdGU2NuQlZjR3h5TkZwV09FYzBURGxOZHowOSIsImlkIjoiZEUxbmNuZFBNblJqVEROVmFWTlFWbXhRTkhoS2R6MDkiLCJmaXJzdF9uYW1lIjoiYVcxV05ITjVSemR6Vm10ak1WUlBSRkF5ZVNzM1VUMDkiLCJlbWFpbCI6Ik5Ga3hNVWhxUXpRNFJ6VlhiR0ppWTJoUk0wMVdNR0pVTlU5clJXSkRWbXRMTTBSU2FHRnhURTFTUlQwPSIsInBob25lIjoiVUhVMFZrOWFTbmQ1ZVcwd1pqUTViRzVSYVc5aGR6MDkiLCJhdmF0YXIiOiJLM1ZzY1M4elMwcDBRbmxrYms4M1JEbHZla05pVVQwOSIsInJlZmVycmFsX2NvZGUiOiJOalZFYzBkM1IyNTBSM3B3VUZWbVRtbHFRVXAwVVQwOSIsImRldmljZV90eXBlIjoiYW5kcm9pZCIsImRldmljZV92ZXJzaW9uIjoiUShBbmRyb2lkIDEwLjApIiwiZGV2aWNlX21vZGVsIjoiU2Ftc3VuZyBTTS1TOTE4QiIsInJlbW90ZV9hZGRyIjoiNTQuMjI2LjI1NS4xNjMsIDU0LjIyNi4yNTUuMTYzIn19.snDdd-PbaoC42OUhn5SJaEGxq0VzfdzO49WTmYgTx8ra_Lz66GySZykpd2SxIZCnrKR6-R10F5sUSrKATv1CDk9ruj_ltCjEkcRq8mAqAytDcEBp72-W0Z7DtGi8LdnY7Vd9Kpaf499P-y3-godolS_7ixClcYOnWxe2nSVD5C9c5HkyisrHTvf6NFAuQC_FD3TzByldbPVKK0ag1UnHRavX8MtttjshnRhv5gJs5DQWj4Ir_dkMcJ4JaVZO3z8j0OxVLjnmuaRBujT-1pavsr1CCzjTbAcBvdjUfvzEhObWfA1-Vl5Y4bUgRHhl1U-0hne4-5fF0aouyu71Y6W0eg'
pwtoken = "pwtoken"

# ────────────────────────────────
# 🔹 AUTO CLASSPLUS TOKEN SYSTEM
# ────────────────────────────────
cptoken = ""

def generate_cptoken():
    """Fetch fresh Classplus token automatically"""
    try:
        token_api = os.getenv("CLASSPLUS_TOKEN_API", "")
        if not token_api:
            return None
        response = requests.get(token_api, timeout=15)
        if response.status_code == 200:
            try:
                data = response.json()
            except ValueError:
                print('[⚠️] Token API returned non-JSON response; continuing without refresh.')
                return None
            token = data.get("cptoken") or data.get("token")
            if token:
                print("[✅] Classplus Token Refreshed Successfully.")
                return token
            else:
                print("[⚠️] Token key not found in API response.")
        else:
            return None
    except Exception as e:
        print(f"[⚠️] Error fetching Classplus token: {e}")
    return None


def refresh_cptoken_periodically():
    """Auto-refresh token every 60 minutes"""
    global cptoken
    while True:
        new_token = generate_cptoken()
        if new_token:
            cptoken = new_token
        time.sleep(3600)  # refresh every 60 min


# Start background refresh thread
threading.Thread(target=refresh_cptoken_periodically, daemon=True).start()

# ────────────────────────────────
# 🔹 OTHER GLOBAL VARIABLES
# ────────────────────────────────
vidwatermark = '/d'
raw_text2 = '480'
quality = '480p'
res = '854x480'
topic = '/d'