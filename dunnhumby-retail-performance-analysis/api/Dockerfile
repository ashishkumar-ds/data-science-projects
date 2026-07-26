FROM python:3.12-slim

WORKDIR /app

# Install dependencies first — this layer only rebuilds when requirements.txt changes,
# not on every code edit, which keeps rebuild-during-development fast.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application package (main.py + model artifacts) as a proper Python package
COPY app/ ./app/

EXPOSE 8000

# $PORT is set by most cloud platforms (Render, Railway, etc.); defaults to 8000 locally
ENV PORT=8000
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT}"]
