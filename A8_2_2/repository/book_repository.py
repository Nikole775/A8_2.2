from A8_2_2.domain.book import Book
from A8_2_2.domain.validators_exceptions import InputError, BookValidatorException


class Book_Repository:

    def __init__(self):
        self._books = []

    def get_all_books(self):
        return self._books[:]

    def create_book(self, book_id, title, author):
        if self.find_book_id(book_id) == False:
            new_book = Book(book_id, title, author)
        else:
            raise BookValidatorException("There already exists a book with this ID")
        return new_book

    def add_generated_book(self, new_book):
        self._books.append(new_book)

    def find_book_id(self, book_id):
        exists = False
        for book in self._books:
            if str(book_id) == str(book.book_id):
                exists = True
        return exists

    def add_new_book(self, book):
        self._books.append(book)

    def remove_book(self, book_id):
        for book in self._books:
            if str(book.book_id) == str(book_id):
                self._books.remove(book)

    def replace_book(self, new_book):
        for book in self._books:
            if str(book.book_id) == str(new_book.book_id):
                book.title = new_book.title
                book.author = new_book.author

    def search_id(self, user_input):
        if not user_input.isdigit() or len(str(user_input)) !=4 :
            raise InputError("That was not a valid ID! :(")
        if self.find_book_id(user_input) == False:
            raise InputError("The book with this ID doesn't exists")

    def search_book_by_id_repo(self, partial_id):
        if not partial_id.isdigit():
            raise InputError("That was not an integer! :(")
        result = []
        for book in self._books:
            if str(partial_id) in str(book.book_id):
                result.append(book)
        return result

    def search_book_by_title_repo(self, partial):
        if partial == '':
            raise InputError("This field cannot be empty!")
        result = []
        for book in self._books:
            if partial.lower() in book.title.lower():
                result.append(book)
        return result

    def search_book_by_author_repo(self, partial):
        if partial == '':
            raise InputError("This field cannot be empty!")
        result = []
        for book in self._books:
            if partial.lower() in book.author.lower():
                result.append(book)
        return result
