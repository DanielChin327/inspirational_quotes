# Backend/app.py
from flask import Flask
from config.db import db
from routes.auth_routes import auth_routes
from routes.quote_routes import quote_routes
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Database Setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/inspirational_quotes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'supersecretkey'  

# Initialize Extensions
db.init_app(app)
JWTManager(app)

# Register Routes
app.register_blueprint(auth_routes, url_prefix='/api/auth')
app.register_blueprint(quote_routes, url_prefix='/api')

# Create Tables
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)