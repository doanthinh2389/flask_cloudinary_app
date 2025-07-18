from flask import Flask, request, render_template, redirect, url_for
import cloudinary
import cloudinary.uploader
import os
import json
from dotenv import load_dotenv

# Load biến môi trường
load_dotenv()

app = Flask(__name__, static_folder='static')

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

# Hàm xóa ảnh khỏi gallery
def remove_from_gallery(image_url):
    gallery = load_gallery()
    if image_url in gallery:
        gallery.remove(image_url)
        with open(GALLERY_FILE, 'w') as f:
            json.dump(gallery, f)
        return True
    return False

@app.route('/delete', methods=['POST'])
def delete_image():
    image_url = request.form.get('image_url')
    if image_url:
        remove_from_gallery(image_url)
    return redirect(url_for('index'))

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
        if file and file.filename != '':
            try:
                upload_result = cloudinary.uploader.upload(
                    file,
                    folder="flask_gallery",  # Thêm ảnh vào thư mục
                    quality="auto",  # Tối ưu chất lượng tự động
                    width=800,  # Giới hạn kích thước
                    crop="limit"
                )
                image_url = upload_result['secure_url']
                save_to_gallery(image_url)
                return redirect(url_for('index'))
            except Exception as e:
                return render_template('upload.html', 
                                   gallery=load_gallery(),
                                   error_message=str(e))

    # GET: lấy danh sách ảnh đã upload
    gallery = load_gallery()
    return render_template('upload.html', gallery=gallery)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)