import { useState } from "react";
import { downloadVideo } from "./services/api";

export default function GlassDownloader() {
  const [url, setUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [downloadLink, setDownloadLink] = useState("");

  const handleDownload = async () => {
    if (!url) {
      setError("Please enter a valid URL");
      return;
    }

    setLoading(true);
    setError("");
    setDownloadLink("");

    try {
      const formData = new FormData();
      formData.append("url", url);

      const response = await downloadVideo(formData);

      if (!response.ok) {
        throw new Error("Failed to download video");
      }

      const data = await response.json();

      const fullUrl = `https://stream-video-downloader.onrender.com${data.download_url}`;

      setDownloadLink(fullUrl);

      // 👉 Auto-trigger download (optional)
      window.open(fullUrl, "_blank");

    } catch (err: unknown) {
      if (err instanceof Error) {
        setError(err.message);
      } else {
        setError("Something went wrong");
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-red-950 via-red-600 to-red-500 flex flex-col items-center justify-items-start px-4">
      <div className="w-full max-w-xl rounded-2xl bg-white/10 backdrop-blur-lg p-8 shadow-xl border border-white/20 ring-1 ring-black mt-12">

        <h1 className="text-3xl font-bold text-white text-center mb-6">
          YouTube Downloader
        </h1>

        <p className="text-white/80 text-center mb-8">
          Paste your link and download in seconds
        </p>

        <div className="flex flex-col gap-4">

          <input
            type="text"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            placeholder="https://youtube.com/watch?v=..."
            className="w-full rounded-lg bg-white/20 px-4 py-3 text-white placeholder-white/70 focus:outline-none focus:ring-2 focus:ring-white"
          />

          <button
            onClick={handleDownload}
            disabled={loading}
            className="w-full rounded-lg bg-white text-black font-semibold py-3 hover:bg-gray-200 transition disabled:opacity-50"
          >
            {loading ? "Downloading..." : "Download Video"}
          </button>

          {error && (
            <p className="text-red-200 text-sm text-center">{error}</p>
          )}

          {downloadLink && (
            <a
              href={downloadLink}
              target="_blank"
              className="text-white underline text-center text-sm"
            >
              Click here if download didn’t start
            </a>
          )}
        </div>
      </div>
    </div>
  );
}