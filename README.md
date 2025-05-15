# Django REST API with SQLite 🚀

This project demonstrates a simple Django REST API application using SQLite as the database. It provides a basic setup for performing CRUD (Create, Read, Update, Delete) operations.

## Features ✨

- **Django Framework**: A robust backend framework for building APIs.
- **SQLite Database**: A lightweight and easy-to-use database.
- **CRUD Operations**: Basic operations for handling data.

## Technologies Used 🛠️

- **Python**: 100% of the codebase is implemented in Python.
- **Django REST Framework**: For creating RESTful APIs.
- **SQLite**: An embedded database for development and testing.

## Setup and Installation 🔧

Follow these steps to set up the project locally:

### Prerequisites 🖥️

- Python 3.7 or higher installed on your system.
- Pip (Python package manager) installed.

### Steps 🪜

1. Clone the repository:
   ```bash
   git clone https://github.com/zeeshank1/django_restapi_curd_sqllite.git
   cd django_restapi_curd_sqllite
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the API at:
   ```
   http://127.0.0.1:8000/
   ```

## API Endpoints 📡

Below are the main endpoints for this REST API:

1. **GET** `/items/` - List all items.
2. **POST** `/items/` - Create a new item.
3. **GET** `/items/<id>/` - Retrieve a specific item by ID.
4. **PUT** `/items/<id>/` - Update an existing item.
5. **DELETE** `/items/<id>/` - Delete a specific item.

Note: Replace `<id>` with the actual ID of the item.

## Contributing 🤝

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push the branch:
   ```bash
   git commit -m "Description of changes"
   git push origin feature-name
   ```
4. Open a pull request.
``
