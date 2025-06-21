FROM python:3.11-slim

# Create app directory
WORKDIR /app

# Install system dependencies (required to build some of pycaret's deps)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy inference script
COPY inferencia.py .

# Default command
ENTRYPOINT ["python", "inferencia.py"]
