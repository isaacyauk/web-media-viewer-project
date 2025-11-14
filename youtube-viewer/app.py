from flask import Flask, render_template, request, jsonify
from models import db
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='../.env')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

# TODO: Add route GET /api/channels - return user's channels
# TODO: Add route POST /api/channels - add new channel
# TODO: Add route DELETE /api/channels/<id> - remove channel
# TODO: Add route GET /api/videos/new - get unseen videos
# TODO: Add route POST /api/check - trigger YouTube check

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)