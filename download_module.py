import yt_dlp
import os
import json
from pathlib import Path
import tempfile


def convert_json_cookies_to_netscape(json_bytes):
    raw = json_bytes.decode("utf-8")

    try:
        data = json.loads(raw)
    except Exception:
        data = json.loads(json.loads(raw))

    if isinstance(data, dict) and "cookies" in data:
        cookies = data["cookies"]
    elif isinstance(data, list):
        cookies = data
    else:
        for v in data.values():
            if isinstance(v, list) and all(isinstance(x, dict) for x in v):
                cookies = v
                break
        else:
            raise ValueError("JSON cookie file format not recognized.")

    lines = ["# Netscape HTTP Cookie File", ""]

    for c in cookies:
        domain = c.get("domain", "")
        if domain and not domain.startswith("."):
            domain = "." + domain

        line = (
            f"{domain}\t"
            f"{'TRUE' if domain.startswith('.') else 'FALSE'}\t"
            f"{c.get('path', '/')}\t"
            f"{'TRUE' if c.get('secure') else 'FALSE'}\t"
            f"{int(c.get('expirationDate') or c.get('expires') or c.get('expiry') or 0)}\t"
            f"{c.get('name','')}\t"
            f"{c.get('value','')}"
        )
        lines.append(line)

    return "\n".join(lines).encode("utf-8")


def download_video(url, output_path, cookies_file=None):

    # Writable temp folder for Streamlit Cloud
    tmp_dir = tempfile.gettempdir()
    cookie_path = None

    # ---- HANDLE COOKIES FIRST ----
    if cookies_file is not None:
        cookie_path = os.path.join(tmp_dir, "temp_cookies.txt")
        cookies_file.seek(0)

        if cookies_file.name.endswith(".txt"):
            with open(cookie_path, "wb") as f:
                f.write(cookies_file.read())

        elif cookies_file.name.endswith(".json"):
            netscape = convert_json_cookies_to_netscape(cookies_file.read())
            with open(cookie_path, "wb") as f:
                f.write(netscape)

    # ---- YT-DLP OPTIONS ----
    ydl_opts = {
        "outtmpl": os.path.join(output_path, "%(title)s.%(ext)s"),
        "format": "bestvideo[ext=mp4][vcodec^=avc]+bestaudio[ext=m4a]/mp4",
        "merge_output_format": "mp4",
    }

    if cookie_path:
        ydl_opts["cookiefile"] = cookie_path

    # ---- DOWNLOAD ----
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])