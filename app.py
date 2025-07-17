from flask import Flask, request, render_template, redirect
import cloudinary
import cloudinary.uploader
import os
import json
from dotenv import load_dotenv

# Load biến môi trường
load_dotenv()

app = Flask(__name__)

# Cấu hình Cloudinary
cloudinary.config(
    cloud_name=os.getenv("CLOUD_NAME"),
    api_key=os.getenv("API_KEY"),
    api_secret=os.getenv("API_SECRET")
)

# Đường dẫn đến file lưu danh sách ảnh
GALLERY_FILE = 'gallery.json'

# Hàm đọc ảnh từ file gallery.json
def load_gallery():
    if os.path.exists(GALLERY_FILE):
        with open(GALLERY_FILE, 'r') as f:
            return json.load(f)
    return []

# Hàm ghi thêm 1 ảnh vào gallery.json
def save_to_gallery(image_url):
    gallery = load_gallery()
    gallery.append(image_url)
    with open(GALLERY_FILE, 'w') as f:
        json.dump(gallery, f)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            upload_result = cloudinary.uploader.upload(file)
            image_url = upload_result['secure_url']
            save_to_gallery(image_url)
            return redirect('/')  # Reload lại để tránh lỗi refresh form

    # GET: lấy danh sách ảnh đã upload
    gallery = load_gallery()
    return render_template('upload.html', gallery=gallery)

if __name__ == '__main__':
    app.run(debug=True)
