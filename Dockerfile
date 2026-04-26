# Use Isaac Lab base image (NVIDIA official)
FROM nvcr.io/nvidia/isaac-lab:2024.1.0

WORKDIR /workspace

# Copy the extension source
COPY . /workspace/go2_extreme_rl_suite

# Install system dependencies (for GUI rendering)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r /workspace/go2_extreme_rl_suite/requirements.txt

# Install our extension in editable mode
RUN pip install -e /workspace/go2_extreme_rl_suite

# Default entrypoint: train script
ENTRYPOINT ["python", "/workspace/go2_extreme_rl_suite/train.py"]