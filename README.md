📦 E‑Commerce API
A RESTful API built with Flask, SQLAlchemy, Marshmallow, and MySQL.
This project manages Users, Products, and Orders with proper relational database design, including One‑to‑Many and Many‑to‑Many relationships.

🎯 Project Overview
This API simulates the backend of a simple e‑commerce system. It supports:

User management

Product management

Order creation

Adding/removing products from orders

Viewing orders by user

Viewing products in an order

The project demonstrates:

Relational database modeling

ORM relationships with SQLAlchemy

Data serialization & validation with Marshmallow

RESTful API design

Testing with Postman

Database verification with MySQL Workbench

🗂 Technologies Used
Python 3

Flask

Flask‑SQLAlchemy

Flask‑Marshmallow

Marshmallow‑SQLAlchemy

MySQL

MySQL Workbench

Postman

🏗 Project Structure
Code
ecommerce_api/
├── app.py
├── models.py
├── schemas.py
├── config.py
├── requirements.txt
├── postman_collection.json
└── README.md
⚙️ Setup Instructions
1. Clone or create project folder
bash
mkdir ecommerce_api
cd ecommerce_api
2. Create and activate virtual environment
Mac/Linux:

bash
python3 -m venv venv
source venv/bin/activate
Windows:

bash
python -m venv venv
venv\Scripts\activate
3. Install dependencies
bash
pip install Flask Flask-SQLAlchemy Flask-Marshmallow marshmallow-sqlalchemy mysql-connector-python
4. Create MySQL database
In MySQL Workbench:

sql
CREATE DATABASE ecommerce_api;
5. Configure database connection
In config.py:

python
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:<YOUR_PASSWORD>@localhost/ecommerce_api"
6. Run the application
bash
python app.py
Visit:
http://127.0.0.1:5000/

🗃 Database Models
User
Field	Type	Notes
id	Integer	Primary Key
name	String	Required
address	String	Required
email	String	Unique, Required
Order
Field	Type	Notes
id	Integer	Primary Key
order_date	DateTime	Defaults to now
user_id	FK	References User
Product
Field	Type	Notes
id	Integer	Primary Key
product_name	String	Required
price	Float	Required
Order_Product (Association Table)
Field	Type	Notes
order_id	FK	References Order
product_id	FK	References Product
Prevents duplicate product entries in the same order.

📦 Marshmallow Schemas
UserSchema

ProductSchema

OrderSchema (includes include_fk = True to expose user_id)

Schemas handle:

Serialization (model → JSON)

Validation (JSON → model)

🚀 API Endpoints
🧍 Users
Method	Endpoint	Description
GET	/users	Get all users
GET	/users/	Get user by ID
POST	/users	Create user
PUT	/users/	Update user
DELETE	/users/	Delete user
📦 Products
Method	Endpoint	Description
GET	/products	Get all products
GET	/products/	Get product by ID
POST	/products	Create product
PUT	/products/	Update product
DELETE	/products/	Delete product
🛒 Orders
Method	Endpoint	Description
POST	/orders	Create order
PUT	/orders//add_product/	Add product to order
DELETE	/orders//remove_product/	Remove product
GET	/orders/user/	Get all orders for a user
GET	/orders//products	Get all products in an order
🧪 Testing Instructions
✔️ Using Postman
Create a Postman Collection

Add a request for each endpoint

Test all CRUD operations

Export the collection as postman_collection.json

Include it in your project folder

✔️ Using MySQL Workbench
Verify tables were created

Run SELECT * FROM users; etc.

Confirm data matches API operations

🎥 Presentation Requirements
Your video must include:

You visible on camera

A short explanation of what the project does

A high‑level explanation of how it works

A live demonstration using Postman

Maximum length: 5 minutes

Upload to Google Drive, set to Anyone with the link → Viewer.

📬 Submission Format
Submit exactly two links:

Code
https://github.com/<username>/<repo>
https://drive.google.com/file/d/<video_id>/view