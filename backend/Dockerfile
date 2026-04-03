# Use latest stable Python
FROM python:3.12-slim

# Prevent Python from writing .pyc files and buffering stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies (packages.txt → ffmpeg)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python -m venv /opt/venv

# Activate venv (for next commands)
ENV PATH="/opt/venv/bin:$PATH"

# Copy dependency files first (for Docker cache optimization)
COPY requirements.txt .
COPY packages.txt .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy application code
COPY . .

# Create downloads folder
RUN mkdir -p downloads

# Expose port (Render/others expect this)
EXPOSE 8000

# Run FastAPI app
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port $PORT"]