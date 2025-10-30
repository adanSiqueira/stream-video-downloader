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
└── .streamlit/
└── config.toml # Optional Streamlit settings
```

## How It Works

1. The user pastes a video URL into the Streamlit app.  
2. The backend calls a helper function (`download_video`) that:  
   - Uses **yt-dlp** to fetch video metadata and formats.  
   - Downloads both the best video and best audio tracks.  
   - Merges them automatically into a single **MP4** file using **ffmpeg**.  
3. The final file is saved and made available locally (on Streamlit Cloud, it’s stored temporarily).  

---

## Future Improvements

- Add download progress tracking.  
- Allow user to choose resolution or format (e.g., **MP3**, **720p**, etc.).  
- Store downloaded files temporarily and provide a direct download link.  
- Add validation for unsupported links or restricted content.  

---

##  Author

**Adan Siqueira**  
🔗 [GitHub Profile](https://github.com/AdanSiqueira)

---

If you like this project, don’t forget to ⭐ **star the repository** to show your support!
