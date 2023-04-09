FROM ghcr.io/coqui-ai/tts:latest

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY main.py main.py
ENTRYPOINT [ "python3", "main.py" ]
