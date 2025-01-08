# Backend/config.py
import os

DB_URI = "mysql+pymysql://root:password@localhost/quotes_db"  # Replace with your MariaDB credentials
SECRET_KEY = os.urandom(24)