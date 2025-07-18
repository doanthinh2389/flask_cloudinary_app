# Base image
FROM python:3.13-slim

# Set workdir
WORKDIR /app

# Copy project files
COPY . .

# Cài gói cần thiết
RUN pip install --no-cache-dir -r requirements.txt

# Mở port Flask (mặc định là 5000)
EXPOSE 5000

# Lệnh chạy app Flask
CMD ["python", "app.py"]
