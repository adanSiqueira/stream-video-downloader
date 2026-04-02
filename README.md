<div align="center">
<h1>stream-video-downloader</h1>

<br/>

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi)
![React](https://img.shields.io/badge/React-Frontend-61DAFB?logo=react)
![TypeScript](https://img.shields.io/badge/TypeScript-Typed-blue?logo=typescript)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-Styling-38B2AC?logo=tailwind-css)
![Vite](https://img.shields.io/badge/Vite-Build-purple?logo=vite)
![yt--dlp](https://img.shields.io/badge/yt--dlp-Downloader-red)
![License](https://img.shields.io/badge/License-MIT-green)

</div>

---

## Overview

**stream-video-downloader** is a full-stack web application that allows users to download videos from YouTube (and other supported platforms) quickly and efficiently.

* Modern UI built with **React + TailwindCSS**
* ⚡ High-performance backend using **FastAPI**
* Powered by **yt-dlp**
* 🔐 Optional support for authenticated downloads via cookies

---

## Architecture

```
Frontend (React + Vite)
        ↓
 FastAPI Backend (API Layer)
        ↓
  yt-dlp (Download Engine)
        ↓
 Local File Storage (/downloads)
```

---

## Project Structure

```
.
├── backend
│   ├── download_module.py
│   ├── main.py
│   ├── schemas.py
│   ├── requirements.txt
│   └── packages.txt
│
├── frontend
│   ├── src/
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │   └── assets/
│   ├── public/
│   └── package.json
│
└── README.md
```

---

## ⚙️ Backend

### Tech Stack

* FastAPI
* yt-dlp
* Pydantic
* FFmpeg (required)

### Features

* Download videos from URL
* Supports cookies (for restricted/private videos)
* Automatic format merging (MP4)
* Secure file serving

---

###📡 API Endpoints

#### `POST /download`

Downloads a video from a given URL.

**Request:**

* `url` (form field) → video URL
* `cookies` (optional file) → `.txt` or `.json`

**Response:**

```json
{
  "filename": "video.mp4",
  "download_url": "/file/video.mp4"
}
```

---

#### `GET /file/{filename}`

Retrieves a downloaded video.

* Streams `.mp4` file
* Includes path validation for security

---

### Core Modules

#### `download_module.py`

* Handles video downloading via yt-dlp
* Converts JSON cookies → Netscape format
* Uses temporary storage (compatible with cloud environments)

#### `main.py`

* FastAPI app definition
* Endpoint logic
* CORS configuration

#### `schemas.py`

* Response validation via Pydantic


---

##  Frontend

### Tech Stack

* React
* TypeScript
* TailwindCSS
* Vite

---

### Features

* Clean modern UI (glassmorphism design)
* Input for video URL
* Download trigger button
* Ready for API integration

---

## 🔐 Cookies Support

This project supports authenticated downloads using cookies.

### Supported Formats:

* `.txt` (Netscape)
* `.json` (browser exports)

### Use Cases:

* Private videos
* Age-restricted content
* Region-locked media

---

## Security Considerations

* Path traversal protection in file serving
* CORS enabled (⚠️ restrict in production)
* Temporary file handling for cookies
* No arbitrary file system access

---

## Working on

* Deploy
* Progress bar (download status)
* Video quality selector
* Audio-only download option
* Queue system (Celery / Redis)
* Authentication system
* Docker support
* Rate limiting

---

##  Workflow

1. User pastes YouTube URL
2. Clicks "Download"
3. Frontend sends request → `/download`
4. Backend processes via yt-dlp
5. File saved in `/downloads`
6. API returns download URL
7. User downloads file

---

