from pydantic import BaseModel

class DownloadResponse(BaseModel):
    filename: str
    download_url: str