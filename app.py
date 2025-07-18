from flask import Flask, request, render_template, redirect, url_for, flash
import cloudinary
import cloudinary.uploader
import os
import json
from dotenv import load_dotenv

# Load biến môi trường
load_dotenv()

app = Flask(__name__, static_folder='static')
app.secret_key = os.getenv("SECRET_KEY") or 'dev-secret-key'

# Cấu hình Cloudinary
cloudinary.config(
    cloud_name=os.getenv("CLOUD_NAME"),
    api_key=os.getenv("API_KEY"),
    api_secret=os.getenv("API_SECRET"),
    secure=True  # Thêm dòng này để luôn dùng HTTPS
)

# Đường dẫn đến file lưu danh sách ảnh
GALLERY_FILE = 'gallery.json'

def load_gallery():
    try:
        if os.path.exists(GALLERY_FILE):
            with open(GALLERY_FILE, 'r') as f:
                return json.load(f)
        return []
    except json.JSONDecodeError:
        return []

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
        try:
            # Xóa ảnh từ Cloudinary
            public_id = image_url.split('/')[-1].split('.')[0]
            cloudinary.uploader.destroy(f"flask_gallery/{public_id}")
            
            # Xóa khỏi gallery local
            remove_from_gallery(image_url)
            flash('Xóa ảnh thành công!', 'success')
        except Exception as e:
            flash(f'Lỗi khi xóa ảnh: {str(e)}', 'error')
    return redirect(url_for('index'))

def save_to_gallery(image_url):
    gallery = load_gallery()
    if image_url not in gallery:  # Tránh trùng lặp
        gallery.append(image_url)
        with open(GALLERY_FILE, 'w') as f:
            json.dump(gallery, f)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Không có file được gửi lên', 'error')
            return redirect(request.url)
            
        file = request.files['file']
        
        if file.filename == '':
            flash('Không có file được chọn', 'error')
            return redirect(request.url)
            
        allowed_extensions = {'png', 'jpg', 'jpeg'}
        if ('.' not in file.filename or 
            file.filename.split('.')[-1].lower() not in allowed_extensions):
            flash('Chỉ chấp nhận file ảnh (PNG, JPG, JPEG)', 'error')
            return redirect(request.url)
        
        try:
            upload_result = cloudinary.uploader.upload(
                file,
                folder="flask_gallery",
                quality="auto",
                width=800,
                crop="limit"
            )
            image_url = upload_result['secure_url']
            save_to_gallery(image_url)
            flash('Upload ảnh thành công!', 'success')
            return redirect(url_for('index'))
            
        except Exception as e:
            flash(f'Lỗi khi upload ảnh: {str(e)}', 'error')
            return redirect(request.url)

    gallery = load_gallery()
    return render_template('upload.html', gallery=gallery)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)