import yt_dlp
import os

def download_video(url, output_path):
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(playlist_index)s - %(title)s.%(ext)s'),
        'format': 'bestvideo[ext=mp4][vcodec^=avc]+bestaudio[ext=m4a]/mp4',
        'merge_output_format': 'mp4',
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    video_url = 'https://www.youtube.com/watch?v=aAy-B6KPld8'
    download_video(video_url, script_dir)