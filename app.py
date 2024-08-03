import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# In-memory database of books
books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
]


# Get all books
@app.route("/books", methods=["GET"])
def get_books():
    logger.info("Fetching all books")
    return jsonify(books)


# Get a specific book by ID
@app.route("/books/<int:id>", methods=["GET"])
def get_book(id):
    logger.info(f"Fetching book with ID: {id}")
    book = next((book for book in books if book["id"] == id), None)
    if book:
        return jsonify(book)
    logger.warning(f"Book with ID {id} not found")
    return jsonify({"message": "Book not found"}), 404


# Create a new book
@app.route("/books", methods=["POST"])
def create_book():
    new_book = request.json
    new_book["id"] = len(books) + 1
    books.append(new_book)
    logger.info(f"Created a new book with ID: {new_book['id']}")
    return jsonify(new_book), 201


# Update an existing book
@app.route("/books/<int:id>", methods=["PUT"])
def update_book(id):
    logger.info(f"Updating book with ID: {id}")
    book = next((book for book in books if book["id"] == id), None)
    if book:
        book.update(request.json)
        logger.info(f"Book with ID {id} updated")
        return jsonify(book)
    logger.warning(f"Book with ID {id} not found")
    return jsonify({"message": "Book not found"}), 404


# Delete a book
@app.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    global books
    logger.info(f"Deleting book with ID: {id}")
    books = [book for book in books if book["id"] != id]
    logger.info(f"Book with ID {id} deleted")
    return jsonify({"message": "Book deleted"}), 204


if __name__ == "__main__":
    app.run(debug=True)
