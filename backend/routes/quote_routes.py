# Backend/routes/quote_routes.py
from flask import Blueprint
from controllers.quote_controller import get_user_quote, add_user_quote, delete_user_quote

quote_routes = Blueprint('quote_routes', __name__)
quote_routes.route('/quote', methods=['GET'])(get_user_quote)
quote_routes.route('/quote', methods=['POST'])(add_user_quote)
quote_routes.route('/quote', methods=['DELETE'])(delete_user_quote)