# Backend/models/quote.py
from config.db import db

class Quote(db.Model):
    __tablename__ = 'quotes'

    quote_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    quote = db.Column(db.Text, nullable=False)
    person = db.Column(db.String(100))