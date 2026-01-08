# Use slim python image for smaller footprint
FROM python:3.12-slim

# Install system dependencies required for audio processing (Whisper)
# ffmpeg is mandatory for openai-whisper
RUN apt-get update && apt-get install -y \
    ffmpeg \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY src/ src/

# Create a user to run the application (security best practice)
RUN useradd -m ambiance && chown -R ambiance /app
USER ambiance

# Expose the port
EXPOSE 8000

# Run the application
# host 0.0.0.0 is required for container networking
CMD ["uvicorn", "ambiance.gateway.server:app", "--host", "0.0.0.0", "--port", "8000"]
