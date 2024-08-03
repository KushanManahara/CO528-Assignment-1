# CO528-Assignment-1

This repository contains the implementation of a simple REST API for managing a collection of books. The API is built using Python's Flask framework and supports basic CRUD operations. The application is also Dockerized for easy deployment.

## Features

- **GET /books**: Retrieve a list of all books.
- **GET /books/{id}**: Retrieve a specific book by its ID.
- **POST /books**: Create a new book.
- **PUT /books/{id}**: Update an existing book by its ID.
- **DELETE /books/{id}**: Delete a book by its ID.

## Setup and Installation

### Prerequisites

- Python 3.x
- Docker

### Local Development

1. **Clone the repository**:

   ```bash
   git clone https://github.com/KushanManahara/CO528-Assignment-1.git
   cd CO528-Assignment-1
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:

   ```bash
   python app.py
   ```

   The application will be accessible at `http://localhost:5000`.

### Docker

1. **Build the Docker image**:

   ```bash
   docker build -t bookstore-api .
   ```

2. **Run the Docker container**:

   ```bash
   docker run -p 5000:5000 bookstore-api
   ```

   The application will be accessible at `http://localhost:5000`.

## API Endpoints

### Get all books

- **URL**: `/books`
- **Method**: `GET`
- **Response**:
  ```json
  [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"}
  ]
  ```

### Get a specific book

- **URL**: `/books/{id}`
- **Method**: `GET`
- **Response**:
  ```json
  {"id": 1, "title": "1984", "author": "George Orwell"}
  ```

### Create a new book

- **URL**: `/books`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald"
  }
  ```
- **Response**:
  ```json
  {
    "id": 3,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald"
  }
  ```

### Update an existing book

- **URL**: `/books/{id}`
- **Method**: `PUT`
- **Request Body**:
  ```json
  {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald"
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald"
  }
  ```

### Delete a book

- **URL**: `/books/{id}`
- **Method**: `DELETE`
- **Response**:
  ```json
  {
    "message": "Book deleted"
  }
  ```

## Logging

Logging is implemented for each endpoint to document actions such as fetching, creating, updating, and deleting books. Logs can be found in the console output where the application is running.

## Contact

For any inquiries, please contact [Kushan Manahara](https://github.com/KushanManahara).