import yt_dlp
import os
import json

def convert_json_cookies_to_netscape(json_bytes):
    """
    Robust converter that accepts:
    - A list of cookie dicts
    - A dict containing {"cookies": [...]}
    - A JSON string inside JSON
    - Various Chrome/Edge extension formats
    """

    raw = json_bytes.decode("utf-8")

    try:
        data = json.loads(raw)
    except Exception:
        # Try to parse again if it's a JSON string inside a JSON string
        data = json.loads(json.loads(raw))

    # Case 1: data is a dict containing {"cookies": [...]}
    if isinstance(data, dict) and "cookies" in data:
        cookies = data["cookies"]

    # Case 2: data is a list directly
    elif isinstance(data, list):
        cookies = data

    # Case 3: data is a dict but not containing cookies → maybe a stringified list?
    elif isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, list) and all(isinstance(x, dict) for x in value):
                cookies = value
                break
        else:
            raise ValueError("JSON cookie file format not recognized.")
    else:
        raise ValueError("JSON cookie file format not supported.")

    # ---- Build Netscape output ----

    lines = ["# Netscape HTTP Cookie File", ""]

    for cookie in cookies:
        if not isinstance(cookie, dict):
            continue

        domain = cookie.get("domain", "")
        if domain and not domain.startswith("."):
            domain = "." + domain

        include_sub = "TRUE" if domain.startswith(".") else "FALSE"
        path = cookie.get("path", "/")
        secure = "TRUE" if cookie.get("secure") else "FALSE"

        expiry = (
            cookie.get("expirationDate")
            or cookie.get("expires")
            or cookie.get("expiry")
            or 0
        )

        name = cookie.get("name", "")
        value = cookie.get("value", "")

        line = f"{domain}\t{include_sub}\t{path}\t{secure}\t{int(expiry)}\t{name}\t{value}"
        lines.append(line)

    return "\n".join(lines).encode("utf-8")



def download_video(url, output_path, cookies_file=None):

    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(playlist_index)s - %(title)s.%(ext)s'),
        'format': 'bestvideo[ext=mp4][vcodec^=avc]+bestaudio[ext=m4a]/mp4',
        'merge_output_format': 'mp4'
        # 'ffmpeg_location': os.path.join(os.path.dirname(__file__), 'ffmpeg')
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # Handle cookies upload
    if cookies_file is not None:
        temp_cookie_path = "temp_cookies.txt"

        # Reset pointer
        cookies_file.seek(0)

        if cookies_file.name.endswith(".txt"):
            with open(temp_cookie_path, "wb") as f:
                f.write(cookies_file.read())

        elif cookies_file.name.endswith(".json"):
            json_bytes = cookies_file.read()
            netscape_bytes = convert_json_cookies_to_netscape(json_bytes)
            with open(temp_cookie_path, "wb") as f:
                f.write(netscape_bytes)

        ydl_opts["cookiefile"] = temp_cookie_path

    # --- RUN YT-DLP ---
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])