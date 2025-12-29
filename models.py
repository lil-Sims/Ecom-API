from datetime import datetime
from app import db
from models import User, Order, Product, order_product
from schemas import UserSchema, ProductSchema, OrderSchema

order_product = db.Table(
    "order_product",
    db.Column("order_id", db.Integer, db.ForeignKey("orders.id"), primary_key=True),
    db.Column("product_id", db.Integer, db.ForeignKey("products.id"), primary_key=True)
)

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    orders = db.relationship("Order", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User {self.id} - {self.email}>"

class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    user = db.relationship("User", back_populates="orders")

    products = db.relationship(
        "Product",
        secondary=order_product,
        back_populates="orders"
    )

    def __repr__(self):
        return f"<Order {self.id} - User {self.user_id}>"

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Float, nullable=False)

    orders = db.relationship(
        "Order",
        secondary=order_product,
        back_populates="products"
    )

    def __repr__(self):
        return f"<Product {self.id} - {self.product_name}>"
