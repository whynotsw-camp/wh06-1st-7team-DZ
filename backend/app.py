from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables from .env in root
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Import routes
from routes.recommend import recommend_bp
from routes.end_kakao import kakao_bp
from routes.naver_search import naver_bp
from routes.instagram import insta_bp

# Register blueprints (modular route registration)
app.register_blueprint(recommend_bp, url_prefix="/api/recommend")
app.register_blueprint(kakao_bp, url_prefix="/api/send-kakao")
app.register_blueprint(naver_bp, url_prefix="/api/naver-review")
app.register_blueprint(insta_bp, url_prefix="/api/instagram-analysis")

# Health check route
@app.route('/')
def index():
    return {"message": "Marketing API Server is running."}, 200

# Run the Flask server
if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(debug=True, port=port)
