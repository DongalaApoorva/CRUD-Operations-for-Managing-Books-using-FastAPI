# Book Management API using FastAPI & MySQL

This project is a simple RESTful API built with **FastAPI** that performs CRUD operations (Create, Read, Update, Delete) on a **MySQL** database of books. It uses JSON for requests and responses and is tested with **Postman**.

---

## Features

- Add a new book
- Retrieve all books or a specific book by ID
- Update existing book details
- Delete a book
- Proper error handling (invalid ID, missing fields, etc.)
- Postman collection included for API testing

---

##  Project Structure

project/
├── main.py
├── models.py
├── schemas.py
├── database.py
├── crud.py
├── requirements.txt
└── README.md

---

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/book-management-api.git
cd book-management-api

2. Create and Activate Virtual Environment
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt
4. Configure MySQL
Create a database in MySQL:

sql
Copy code
CREATE DATABASE books_db;
Import the sample CSV using MySQL Workbench:

Use books_dataset_mysql_import.csv

Table: books

Columns: id, title, author, genre, publication_year

5. Set Up Database Connection
Edit database.py with your credentials:

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://username:password@localhost/books_db"
## Running the Application
uvicorn main:app --reload --port 8000
Visit the Swagger Docs:
http://127.0.0.1:8000/docs
## API Endpoints
Method	Endpoint	Description
GET	/books	Retrieve all books
GET	/books/{book_id}	Retrieve a book by ID
POST	/books	Add a new book
PUT	/books/{book_id}	Update book details
DELETE	/books/{book_id}	Delete a book

## Sample POST Request

POST /books
Content-Type: application/json

{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "genre": "Classic",
  "publication_year": 1925
}
## Response
{
  "message": "Book added successfully.",
  "book": {
    "id": 1,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "genre": "Classic",
    "publication_year": 1925
  }
}
## Testing the API with Postman
Use the provided Book-Postman-Collection.json file

Set header:

Content-Type: application/json
Test all endpoints with appropriate body data

## Error Handling
Returns informative error messages for:

Invalid Book IDs (404)

Missing or malformed JSON (400)

Internal errors (500)

