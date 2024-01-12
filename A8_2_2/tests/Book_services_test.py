from unittest.case import TestCase
from A8_2_2.domain.validators_exceptions import BookValidatorException, ClientValidatorException, InputError
from A8_2_2.repository.book_repository import Book_Repository
from A8_2_2.services.book_services import Book_services



import unittest

class TestBookServices(unittest.TestCase):
    def setUp(self):
        self.book_repository = Book_Repository()
        self.book_services = Book_services(self.book_repository)

    def test_add_book_valid(self):
        # Test adding a valid book
        book_id = "1234"
        self.book_services.add_book(book_id, "The Great Gatsby", "F. Scott Fitzgerald")
        # Check if the book is in the repository
        self.assertTrue(self.book_services.find_book_id_services(book_id))

    def test_add_book_existing_id(self):
        # Test adding a book with an existing ID
        self.book_services.add_book("5678", "To Kill a Mockingbird", "Harper Lee")
        # Try adding another book with the same ID "5678", it should raise an exception
        with self.assertRaises(BookValidatorException):
            self.book_services.add_book("5678", "New Book", "New Author")

    def test_add_book_invalid_id(self):
        # Test adding a book with an invalid ID
        # Try adding a book with a non-numeric ID
        with self.assertRaises(BookValidatorException):
            self.book_services.add_book("abcd", "Invalid Book", "Invalid Author")
        # Try adding a book with an ID that is not 4 digits
        with self.assertRaises(BookValidatorException):
            self.book_services.add_book("12", "Invalid Book", "Invalid Author")

    def test_add_book_empty_title_author(self):
        # Test adding a book with empty title and author fields
        with self.assertRaises(BookValidatorException):
            self.book_services.add_book("1234", "", "")

    """def test_update_book_valid(self):
        # Add a book to the repository for testing
        book_id = "1234"
        self.book_services.add_book(book_id, "The Old Book", "Old Author")

        # Update the book with new details
        new_title = "Updated Book"
        new_author = "Updated Author"
        self.book_services.update_book(book_id, new_title, new_author)

        # Check if the book is updated in the repository
        book_found = self.book_repository.find_book_id(book_id)

        # If the book is found, check if it's a Book object before accessing attributes
        if book_found and isinstance(book_found, Book):
            self.assertEqual(book_found.title, new_title)  # Check if the title is updated
            self.assertEqual(book_found.author, new_author)  # Check if the author is updated
        elif not book_found:
            # If the book is not found, the test case should pass (no further checks needed)
            pass
        else:
            self.fail("Expected a Book object, but found a boolean value.")"""

    def test_update_book_invalid(self):
        # Try updating a book with invalid details
        book_id = "5678"
        self.book_services.add_book(book_id, "Another Book", "Another Author")
        with self.assertRaises(BookValidatorException):
            self.book_services.update_book(book_id, "", "New Author")

    def test_delete_book_valid(self):
        # Add a book to the repository for testing
        book_id = "1234"
        self.book_services.add_book(book_id, "Test Book", "Test Author")
        # Delete the book using delete_book
        self.book_services.delete_book(book_id)
        # Ensure the book is removed from the repository
        result = self.book_services.find_book_id_services(book_id)
        print("Result:", result)
        # Check if result is False (indicating the book is not found)
        self.assertFalse(result)
    def test_delete_book_invalid_id(self):
        with self.assertRaises(InputError):
            self.book_services.delete_book("invalid_id")

    def test_delete_book_nonexistent(self):
        with self.assertRaises(InputError):
            self.book_services.delete_book("9999")

    def test_list_books_with_books(self):
        # Add a few books to the repository for testing
        self.book_services.add_book("1234", "Book 1", "Author 1")
        self.book_services.add_book("5678", "Book 2", "Author 2")
        # Ensure that the list_books method returns the correct list of books
        expected_result = self.book_repository.get_all_books()
        result = self.book_services.list_books()
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
