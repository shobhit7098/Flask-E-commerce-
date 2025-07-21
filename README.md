<<<<<<< HEAD
 
=======
# Flask-E-commerce
# 🛒 E-commerce Backend API (FastAPI + MongoDB)

This is a simple e-commerce backend built using **FastAPI** and **MongoDB (Atlas)**. It includes the following REST APIs:

- ✅ Create Product
- 📃 List Products with filters (name, size, pagination)
- 🛍️ Create Order
- 📦 List Orders by User

---

## 🚀 Features

- FastAPI async APIs
- MongoDB Atlas using Motor (async driver)
- Basic pagination and filtering support
- RESTful design

---

## 🧱 Project Structure
.
├── app/
│ ├── main.py # FastAPI app entry point
│ ├── db.py # MongoDB connection and collections
│ ├── models.py # Pydantic models for request and response
│ ├── product.py # Product APIs
│ └── order.py # Order APIs
├── requirements.txt
└── README.md

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

### 1. 📦 Clone the repository

```bash
git clone https://github.com/yourusername/Flask-E-commerce-.git
cd Flask-E-commerce-
2. 🐍 Create and activate a virtual environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate      # On Linux/Mac
venv\Scripts\activate         # On Windows
3. 📦 Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. 🔐 Setup MongoDB
Make sure to update your MongoDB URI in app/db.py:

python
Copy
Edit
MONGO_URI = "your_mongodb_atlas_uri"
You can get a FREE cluster URI from MongoDB Atlas.

▶️ Run the Application
bash
Copy
Edit
uvicorn app.main:app --reload
Server will start at:
👉 http://127.0.0.1:8000
