import yt_dlp
import os
import json
from pathlib import Path
import tempfile


def convert_json_cookies_to_netscape(json_bytes):
    """
    Convert a YouTube/Chrome/Edge JSON cookie export into Netscape cookie format.

    This function accepts multiple cookie formats exported by browser extensions,
    including:
        - A raw list of cookie dictionaries
        - A dict containing {"cookies": [...]}
        - A JSON string inside a JSON blob (common in some extensions)
        - Chrome/Edge extension export formats

    It produces a Netscape-compatible cookie file (required by yt-dlp),
    converting relevant fields such as domain, path, secure flag, expiration
    timestamp, name, and value.

    Args:
        json_bytes (bytes):
            RAW bytes read from a cookie file (uploaded in Streamlit).
            Must represent a JSON array or dict containing cookie structures.

    Returns:
        bytes:
            A UTF-8 encoded string representing the cookie data in Netscape format.

    Raises:
        ValueError:
            If the JSON structure cannot be parsed into a known cookie format.

    Notes:
        - The Netscape format is required for yt-dlp's `--cookies` / `cookiefile`.
        - Unknown fields are ignored; missing fields are safely defaulted.
    """
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
    """
    Download a YouTube video using yt-dlp with optional authenticated cookies.

    This function:
        1. Converts an uploaded Streamlit cookie file (.txt or .json) to a
           temporary Netscape cookie file inside the system's temp directory.
        2. Configures yt-dlp to use the cookie file if provided.
        3. Downloads the video using a format that prioritizes
           AVC/H.264 + M4A audio and merges output into MP4.

    This design is compatible with Streamlit Cloud restrictions—files can only
    be written inside the temporary directory, not the repository folder.

    Args:
        url (str):
            A valid YouTube video URL.
        output_path (str):
            Path to a folder where the final video file will be saved.
        cookies_file (UploadedFile, optional):
            File uploaded via Streamlit (`st.file_uploader`).
            Accepts either a `.txt` Netscape cookie file or a `.json` export
            from browser extensions.

    Returns:
        None
            The video is downloaded directly to `output_path`.

    Raises:
        yt_dlp.utils.DownloadError:
            If the video cannot be downloaded (blocked, invalid URL, etc.).
        ValueError:
            If the cookies file is not in a supported format.

    Notes:
        - Runs *one* download only (no duplicates).
        - Ensures predictable formats (AVC video + AAC/M4A audio).
        - Uses system temp directory for cookie handling:
              tempfile.gettempdir()
        - Works identically locally and on Streamlit Cloud.
    """

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