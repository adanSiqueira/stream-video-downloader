import streamlit as st
import os
from pathlib import Path
from download_module import download_video

st.set_page_config(page_title="Video Downloader", page_icon="🎥", layout="centered")

st.title("YouTube Video Downloader")

st.markdown("""
Paste a YouTube link below, upload your cookie settings file (.json or .txt) and download the video as MP4.

### 🔐 Why do I need a cookie file?
To the app access YouTube videos it requires login, to guarantee it`s not a bot.
To download these videos, you must provide a **cookie file**, which lets the downloader use *your* YouTube session.

Your login information is **never stored**.
""")

# URL input
video_url = st.text_input("🔗 Enter video URL", placeholder="https://www.youtube.com/watch?v=...")

# Cookie uploader
st.markdown("### 📄 Upload your cookie file")
cookiefile = st.file_uploader(
    "Accepted formats: .txt or .json",
    type=["txt", "json"]
)

# Guide
with st.expander("ℹ️ How to get your YouTube cookies file (Microsoft Edge)"):
    st.markdown("""
To download restricted videos, you must export your YouTube cookies.

### **Step-by-step**

#### **1. Install the J2TEAM Cookies extension**
👉 https://microsoftedge.microsoft.com/addons/detail/j2team-cookies/lmakhegealefmkbnagibiebebncemhgn

Click **Get** → **Add extension**

---

#### **2. Open YouTube**
Go to https://youtube.com and make sure you are logged in.

---

#### **3. Export the cookies**
1. Click the **J2TEAM Cookies** extension (upper-right corner)  
2. Click **Export**  
3. Choose **“Export as File”**  
4. Save the file (`cookies.json`)

---

#### **4. Upload that file here**
Use the uploader above.

---

🔒 **Your cookies are used only for authentication and are never stored.**
""")

# Download button
if st.button("Download"):
    if not video_url.strip():
        st.warning("⚠️ Please enter a video URL first.")
    else:
        try:
            output_path = Path("downloads")
            output_path.mkdir(exist_ok=True)

            with st.spinner("Downloading... ⏳"):
                download_video(video_url, str(output_path), cookies_file=cookiefile)

            st.success("✅ Download complete!")

            files = sorted(output_path.glob("*.mp4"), key=os.path.getmtime, reverse=True)
            if files:
                latest = files[0]

                st.video(str(latest))

                with open(latest, "rb") as file:
                    st.download_button(
                        label="⬇️ Download File",
                        data=file,
                        file_name=latest.name,
                        mime="video/mp4"
                    )

        except Exception as e:
            st.error(f"❌ Error: {e}")