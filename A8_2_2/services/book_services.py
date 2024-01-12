from A8_2_2.repository.book_repository import Book_Repository, Book
from random import randint, choice
from A8_2_2.domain.validators_exceptions import BookValidator


class Book_services:

    def __init__(self, repository):
        self.__repository = repository
        self.generate_n_books()


    def generate(self):
        # generate book_id
        book_id_used = []
        book_id = randint(1000, 9999)
        while book_id in book_id_used:
            book_id = randint(1000, 9999)
        book_id_used.append(book_id)

        # generate title

        titles = ["Pride and Prejudice", "1984", "Crime and Punishment", "Hamlet", "One Hundred Years of Solitude",
                  "Anna Karenina", "The Odyssey", "The Stranger", "The Brothers Karamazov", "Lolita",
                  "The Old Man and The Sea", "War and Peace", "Great Expectations", "Don Quixote", "The Iliad",
                  "Madame Bovary", "The Trial"]
        title = choice(titles)

        # generate authors
        names = ["Jane Austen", "George Orwell", "Fyodor Dostoevsky", "William Shakespeare", "Gabriel Garcia",
                 "Leo Tolstoy", "Homer", "Albert Camus", "Vladimir Nabokov", "Ernest Hemingway", "Charles Dickens",
                 "Miguel de Cervantes", "Gustave Flaubert", "Franz Kafka", "Dante Alighieri", "Herman Melville"]
        author = choice(names)

        return self.__repository.create_book(book_id, title, author)

    def generate_n_books(self):
        for i in range(20):
            self.__repository.add_generated_book(self.generate())

    def delete_book(self, book_id):
        """Inputs:
            book_id (string): The ID of the book to be deleted.
            Validates the book_id using the search_id method of the repository.
            Removes the book with the specified book_id using the remove_book method of the repository.
            Raises an InputError if the book_id is not a valid ID (not a 4-digit number) or if the book with the given book_id does not exist.
            Removes the book with the specified book_id from the repository."""
        self.__repository.search_id(book_id)
        self.__repository.remove_book(book_id)

    def list_books(self):
        """Inputs:
            None
            Retrieves the list of all books from the repository using the get_all_books method.
            Returns a list of all books in the repository."""
        return self.__repository.get_all_books()

    def add_book(self, book_id, title, author):
        """
         It verifyes if there exists a book with this new ID in the repository,if not it creates a book
        object with a new book_id, the title(parameter), author(parameter). Then it saves the book in
        the repository if it is valid.
            :param title: (string) title of the book
            :param author: (string title of the book
            Raises BookValidatorException if book is not valid.
            :return:-
        """
        book = self.__repository.create_book(book_id, title, author)
        BookValidator.validate_book(book)
        self.__repository.add_new_book(book)

    def update_book(self, book_id, title, author):
        """Inputs:
            book_id (string): The ID of the book to be updated.
            title (string): The new title for the book.
            author (string): The new author for the book.
            It creates a new book object with the provided book_id, title, and author.
            Validates the new book using the BookValidator.validate_book method.
            Calls the replace_book method of the repository to update the book with the new details.
            Raises a BookValidatorException if the new book is not valid."""
        new_book = Book(book_id, title, author)
        BookValidator.validate_book(new_book)
        self.__repository.replace_book(new_book)

    def search_id_services(self, book_id):
        self.__repository.search_id(book_id)

    def search_book_by_id(self, partial_id):
        return(self.__repository.search_book_by_id_repo(partial_id))

    def search_book_by_title(self, partial_title):
        return(self.__repository.search_book_by_title_repo(partial_title))

    def search_book_by_author(self, partial_author):
        return (self.__repository.search_book_by_author_repo(partial_author))

    def find_book_id_services(self, book_id):
        return self.__repository.find_book_id(book_id)