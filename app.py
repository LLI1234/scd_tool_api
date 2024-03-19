from flask import Flask
from database import db
from routes.user import user_routes
from routes.session import session_routes, login_manager
from routes.center import center_routes
from routes.match import match_routes
from routes.insurance import insurance_routes
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ["APP_SECRET_KEY"]

# database
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["SQLALCHEMY_DATABASE_URI"]
db.init_app(app)
login_manager.init_app(app)

with app.app_context():
    db.create_all()

# routes
app.register_blueprint(user_routes)
app.register_blueprint(session_routes)
app.register_blueprint(center_routes)
app.register_blueprint(match_routes)
app.register_blueprint(insurance_routes)

if __name__ == "__main__":
    app.run(debug=True)
