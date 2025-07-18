# 📸 Flask Cloudinary Upload App

A simple and responsive Flask web app to **upload and view images** stored securely on **Cloudinary**.

CI/CD is fully automated with **GitHub Actions**, and the app is hosted 24/7 on **Render**.

🌐 Live demo: [https://flask-gallery-app.onrender.com](https://flask-gallery-app.onrender.com)  
📦 GitHub repo: [github.com/doanthinh2389/flask_cloudinary_app](https://github.com/doanthinh2389/flask_cloudinary_app)

---

## 🚀 Features

✅ Upload image files through browser  
✅ Store and retrieve images from Cloudinary  
✅ Display uploaded images as a gallery  
✅ Responsive UI with custom CSS/JS  
✅ Automatically deployed via GitHub Actions → Render  
✅ Supports Docker containerization for portability  

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask  
- **Cloud Storage**: Cloudinary API  
- **CI/CD**: GitHub Actions  
- **Hosting**: Render.com  
- **Containerization**: Docker  
- **Secrets Management**: `.env` + `.gitignore`

---

## 📁 Project Structure

flask_cloudinary_app/
│
├── app.py # Flask app logic
├── .env # Cloudinary credentials (NOT pushed)
├── requirements.txt # Python dependencies
├── gallery.json # Local record of image URLs
├── Dockerfile # For optional containerized deployment
├── templates/ # HTML templates (upload.html)
├── static/ # CSS, JS, images
├── .github/workflows/ # GitHub Actions CI/CD pipeline
│ └── deploy.yml
└── README.md # This file

---

## 💻 How to Run Locally

```bash
# Clone the repo
git clone https://github.com/doanthinh2389/flask_cloudinary_app.git
cd flask_cloudinary_app

# Optional: create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set Cloudinary credentials in .env
CLOUD_NAME=your_cloud_name
API_KEY=your_api_key
API_SECRET=your_api_secret

# Run the app
python app.py

## 🖼️ Screenshot

![App UI](./static/images/screenshot.png)


🐳 Run with Docker (Optional)
docker build -t flask-app .
docker run -p 5000:5000 --env-file .env flask-app
⚙️ CI/CD Workflow
Each push to main triggers:

GitHub Actions to build the app.

Auto-deploy to Render.

App is always online at:
🔗 https://flask-gallery-app.onrender.com

🧠 Author
👤 Đoàn Quốc Thịnh
📧 Email: doanquoc@example.com
🔗 GitHub: doanthinh2389

🧾 What I Learned
How to integrate Flask with third-party APIs (Cloudinary).

Automating CI/CD using GitHub Actions.

Deploying apps to cloud platforms like Render.

Managing secrets with environment variables and Docker.

Writing professional project documentation.