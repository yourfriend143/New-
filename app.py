import os
from flask import Flask

app = Flask(__name__)

@app.get("/")
def hello_world():
    return "DRM Bot is running", 200

@app.get("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8000")))
