export default function GlassDownloader() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-red-950 via-red-600 to-red-500 flex items-center justify-center px-4">
      
      <div className="w-full max-w-xl rounded-2xl bg-white/10 backdrop-blur-lg p-8 shadow-xl border border-white/20 ring-1 ring-black">
        
        <h1 className="text-3xl font-bold text-white text-center mb-6">
          YouTube Downloader
        </h1>

        <p className="text-white/80 text-center mb-8">
          Paste your link and download in seconds
        </p>

        <div className="flex flex-col gap-4">
          <input
            type="text"
            placeholder="https://youtube.com/watch?v=..."
            className="w-full rounded-lg bg-white/20 px-4 py-3 text-white placeholder-white/70 focus:outline-none focus:ring-2 focus:ring-white"
          />

          <button className="w-full rounded-lg bg-white text-black font-semibold py-3 hover:bg-gray-200 transition">
            Download Video
          </button>
        </div>
      </div>
    </div>
  );
}