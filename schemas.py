from marshmallow import fields, validates, ValidationError
from app import ma
from models import User, Order, Product

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

    @validates("email")
    def validate_email(self, value):
        if "@" not in value:
            raise ValidationError("Invalid email format.")

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True

    @validates("price")
    def validate_price(self, value):
        if value < 0:
            raise ValidationError("Price must be non-negative.")

class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        load_instance = True
        include_fk = True

    user_id = fields.Integer(required=True)
