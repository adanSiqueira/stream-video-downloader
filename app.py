import streamlit as st
import os
from pathlib import Path
from download_module import download_video 

st.set_page_config(page_title="Video Downloader", page_icon="🎥", layout="centered")

st.title("🎥 YouTube Video Downloader")
st.write("Paste a YouTube or video link below and download the video as MP4.")

#Input field
video_url = st.text_input("Enter video URL", placeholder="https://www.youtube.com/watch?v=...")

#Button
if st.button("Download"):
    if not video_url.strip():
        st.warning("⚠️ Please provide a valid video URL.")
    else:
        try:
            # Create output folder
            output_path = Path("downloads")
            output_path.mkdir(exist_ok=True)

            with st.spinner("Downloading... ⏳"):
                download_video(video_url, str(output_path))
            
            st.success("✅ Download complete!")
            
            # Find latest file downloaded
            files = sorted(output_path.glob("*.mp4"), key=os.path.getmtime, reverse=True)
            if files:
                latest = files[0]
                st.video(str(latest))  # show preview
                with open(latest, "rb") as file:
                    st.download_button(
                        label="⬇️ Download File",
                        data=file,
                        file_name=latest.name,
                        mime="video/mp4"
                    )
        except Exception as e:
            st.error(f"❌ Error: {e}")
