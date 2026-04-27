FROM nvidia/cuda:12.2.0-devel-ubuntu22.04

RUN apt-get update && apt-get install -y \
    python3.10 python3-pip git wget \
    libgl1-mesa-glx libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .
RUN pip3 install --no-cache-dir -e .

ENTRYPOINT ["python3", "train.py"]
