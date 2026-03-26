FROM python:3.11-slim

WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything (including the app/ folder)
COPY . .

# Create data directory
RUN mkdir -p app/data

# IMPORTANT: Run from inside the app folder
CMD ["python", "app/main.py"]