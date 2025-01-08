# Backend/routes/auth_routes.py
from flask import Blueprint
from controllers.auth_controller import register_user, login_user

auth_routes = Blueprint('auth_routes', __name__)
auth_routes.route('/register', methods=['POST'])(register_user)
auth_routes.route('/login', methods=['POST'])(login_user)