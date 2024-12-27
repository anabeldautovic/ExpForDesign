# Start from an official Python 3.9 image
FROM python:3.9-slim

LABEL maintainer="Francisco B. Valero <franbvalero@gmail.com>"
LABEL description="Docker image for experimentation"

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    curl \
    git \
    libsqlite3-0 \
    libsqlite3-dev \
    sqlite3 \
    tar \
    wget \
    less \
    vim \
    g++ \
    build-essential \
    make \
    protobuf-compiler \
    libprotobuf-dev \
    dos2unix \
    && apt-get clean

# Upgrade pip
RUN pip install --upgrade pip

# Install PyTorch (CPU version compatible with Python 3.9)
RUN pip install torch==1.8.0+cpu torchvision==0.9.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

# Install other dependencies
RUN pip install numpy==1.20.3
RUN pip install daal==2021.2.3
RUN pip install radboud-el
RUN pip install git+https://github.com/informagi/REL
RUN mkdir -p /.rel_cache /.flair
RUN chmod 777 /.rel_cache /.flair

COPY requirements.txt ./ 
RUN pip install -r requirements.txt

# Install NLTK data
RUN mkdir -p /usr/local/share/nltk_data
RUN [ "python", "-c", "import nltk; nltk.download('punkt', download_dir='/usr/local/share/nltk_data'); import nltk; nltk.download('averaged_perceptron_tagger', download_dir='/usr/local/share/nltk_data'); nltk.download('stopwords', download_dir='/usr/local/share/nltk_data'); nltk.download('wordnet', download_dir='/usr/local/share/nltk_data'); nltk.download('omw-1.4', download_dir='/usr/local/share/nltk_data')"]

WORKDIR /workspace
