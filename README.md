<h1 align="center">StreamVideo Downloader </h1>
<p align="center">
  <a href="https://streamlit.io/">
    <img src="https://img.shields.io/badge/Framework-Streamlit-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit">
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white" alt="Python">
  </a>
  <a href="https://github.com/yt-dlp/yt-dlp">
    <img src="https://img.shields.io/badge/yt--dlp-Video_Downloader-orange?logo=youtube&logoColor=white" alt="yt-dlp">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  </a>
</p>

<p align="center">
  <strong> Link:</strong>  
  <a href="https://stream-video-downloader.streamlit.app/">
    https://stream-video-downloader.streamlit.app/
  </a><br>
  Simply paste a video URL (like a YouTube link) and click <strong>Download</strong>.
</p>

---

##  Overview

**StreamVideo Downloader** is a web app built with **Streamlit** and **yt-dlp**, designed to let you **download videos directly from the web** (e.g., YouTube, Vimeo, etc.) with just a link — no command-line, no setup hassles.

It wraps the power of `yt-dlp` in a clean, intuitive web interface, enabling users to paste any video URL and instantly start the download process right from their browser.

---

## Features

- **Paste any video URL** — works with major platforms like YouTube, Vimeo, and others supported by `yt-dlp`.
-  **Smart format selection** — automatically downloads the best available video and audio quality (merged as MP4).
- **Fast and reliable** — powered by `yt-dlp`, one of the most efficient open-source video downloaders.
-  **Automatic file naming** — organizes your downloads by playlist index and title.
- **Works directly on the cloud** — no need to install anything locally.
- **Lightweight and portable** — just a few lines of Python and Streamlit.

---

## Stack

| Layer | Technology | Description |
|-------|-------------|-------------|
|  Backend | **Python 3.10+** | Core language for logic and processing |
| Web Framework | **Streamlit** | Fast, lightweight web UI for data and ML apps |
|  Video Engine | **yt-dlp** | Handles video extraction, merging, and conversion |
| System Dependency | **ffmpeg** | Merges video/audio streams into MP4 format |

---

## Project Structure
```
stream-video-downloader/
│
├── app.py # Streamlit frontend
├── downloader.py # Core download logic using yt-dlp
├── requirements.txt # Python dependencies
├── packages.txt # OS-level dependency (ffmpeg)
├── README.md # Project documentation
```

## How It Works

The app is split into **two main components** — the Streamlit UI (`app.py`) and the download engine (`downloader.py`).
Together, they handle URL input, cookie conversion, and safe video downloading using `yt-dlp`.

#### **1. User provides a video URL (and optionally a cookies file)**

Inside the Streamlit interface, the user enters any supported video link and can optionally upload a **cookies file** (`.txt` or `.json`).
This is useful for downloading **age-restricted or region-locked videos**.

#### **2. Cookies (if provided) are normalized**

When a `.json` cookies file is uploaded:

* The function `convert_json_cookies_to_netscape()`
  converts it into the **Netscape cookie format**, which is required by `yt-dlp`.
* Both `.txt` and `.json` cookies are written to a **temporary, writable directory**,
  ensuring compatibility with Streamlit Cloud’s filesystem.

#### **3. The download engine prepares yt-dlp**

The `download_video()` function builds the `yt_dlp` configuration:

* Saves files using an output template based on the video title
* Selects the best **MP4-compatible** video stream (AVC/H.264)
* Selects the best **M4A audio** stream
* Ensures automatic merging into a single **MP4** file
* Injects the converted cookie file when needed

This guarantees compatibility across browsers and platforms.

#### **4. yt-dlp downloads and merges video/audio**

`yt-dlp`:

1. Fetches metadata
2. Downloads the chosen video and audio formats
3. Uses **ffmpeg** to safely merge them into a final MP4
4. Saves the output inside your chosen folder (`downloads/` by default)

#### **5. Streamlit presents the final file**

After the backend finishes:

* The file appears in the UI
* Streamlit provides a button so the user can **download the MP4 directly**
---

## Future Improvements
 
- Allow user to choose resolution or format (e.g., **MP3**, **720p**, etc.).  
- Store downloaded files temporarily and provide a direct download link.  

---

##  Author

**Adan Siqueira**  
🔗 [GitHub Profile](https://github.com/AdanSiqueira)

---

If you like this project, don’t forget to ⭐ **star the repository** to show your support!


