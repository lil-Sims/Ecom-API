from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import Config

db = SQLAlchemy()
ma = Marshmallow()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)

    from models import User, Order, Product, order_product

    with app.app_context():
        db.create_all()

    user_schema = UserSchema()
    users_schema = UserSchema(many=True)
    product_schema = ProductSchema()
    products_schema = ProductSchema(many=True)
    order_schema = OrderSchema()
    orders_schema = OrderSchema(many=True)


    register_routes(app)

    return app

def register_routes(app):

    @app.route("/")
    def index():
        return {"message": "E-commerce API is running"}

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
