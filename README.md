# Blog Project

## Overview
This is a Django-based blog application that allows users to create, read, update, and delete blog posts. The project is structured to follow Django's best practices and includes features such as user authentication, permissions, and a REST API for interacting with the blog data.

## Features
- Create, read, update, and delete blog posts.
- User authentication and permissions.
- REST API for blog operations.
- SQLite database for data storage.


## Requirements
- Python 3.8+
- Django 4.0+


## Testing
To run the tests, execute:
```bash
python manage.py test
```


## Admin Panel

The project includes a Django Admin Panel for managing blog posts and other models. The admin panel provides an easy-to-use interface for administrators to perform CRUD operations on the database.


### Features of the Admin Panel
- Manage blog posts (create, update, delete).
- Manage users and permissions.
- View and manage other models registered in the admin site.

### Additional Features of the Admin Panel
- Filtering options for blog posts and other models to easily find specific records based on criteria.

## API Documentation

The project includes Swagger API documentation for the REST API endpoints. Swagger provides an interactive interface to explore and test the API.

### Accessing Swagger
1. Start the development server:
   ```bash
   python manage.py runserver
   ```
2. Open your browser and navigate to `http://127.0.0.1:8000/api/docs/`.

You can view all available endpoints, their request/response formats, and test them directly from the Swagger UI.
