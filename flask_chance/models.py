from datetime import datetime
from enum import unique
from flask_chance import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    cpf = db.Column(db.String(12), unique=True, nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    orders = db.relationship('Order', backref='client', lazy=True)

    def __repr__(self):
        return f"User('{self.name}','{self.email}', '{self.cpf}', '{self.phone}')"


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_cafe = db.Column(db.Integer, nullable = False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    quant_cafe = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Order('{self.type_cafe}', '{self.date_posted}', '{self.quant_cafe}', '{self.price}')"
