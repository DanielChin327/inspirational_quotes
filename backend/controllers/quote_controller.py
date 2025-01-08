# Backend/controllers/quote_controller.py
from flask import request, jsonify
from models.quote import Quote
from config.db import db
from flask_jwt_extended import jwt_required, get_jwt_identity

@jwt_required()
def get_user_quote():
    user_id = get_jwt_identity()
    quote = Quote.query.filter_by(user_id=user_id).order_by(db.func.random()).first()
    if quote:
        return jsonify({"quote": quote.quote, "person": quote.person})
    return jsonify({"message": "No quotes available"}), 404

@jwt_required()
def add_user_quote():
    data = request.get_json()
    user_id = get_jwt_identity()
    new_quote = Quote(user_id=user_id, quote=data['quote'], person=data['person'])
    db.session.add(new_quote)
    db.session.commit()
    return jsonify({"message": "Quote added successfully"}), 201

@jwt_required()
def delete_user_quote():
    user_id = get_jwt_identity()
    quote = Quote.query.filter_by(user_id=user_id).first()
    if quote:
        db.session.delete(quote)
        db.session.commit()
        return jsonify({"message": "Quote deleted"})
    return jsonify({"message": "No quotes available"}), 404