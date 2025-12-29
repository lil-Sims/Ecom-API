import os

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:<0306>@localhost/ecommerce_api"
    SQLALCHEMY_TRACK_MODIFICATIONS = False