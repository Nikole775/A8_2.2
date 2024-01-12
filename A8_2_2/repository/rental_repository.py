from A8_2_2.domain.rental import Rental
from A8_2_2.domain.validators_exceptions import RepositoryError, ClientValidator, BookValidator, InputError
import datetime
class Rental_Repository:

    def __init__(self):
        self._rentals = []
        self._rented_books_ids = []

    def add_generated_rentals(self, rental):
        book_id = str(rental.book_id)
        """if rental.returned_date is None:"""
        if datetime.date.today() - rental.rented_date < datetime.timedelta(weeks=2):
            self._rented_books_ids.append(book_id)
        self._rentals.append(rental)

    def add_new_rental(self, rent_id, book_id, client_id, rented_date):
        self._rented_books_ids.append(book_id)
        rental = Rental(rent_id, book_id, client_id, rented_date)
        self._rentals.append(rental)

    def get_all_rentals(self):
        return self._rentals[:]

    def get_all_rented_books(self):
        return self._rented_books_ids[:]

    def verify_existent_client(self, client_id):
        ClientValidator.verify_data(client_id)
        ok = False
        for rent in self._rentals:
            if str(rent.client_id) == str(client_id):
                ok = True
        return ok

    def search_rental(self, rent_id: int):
        BookValidator.verify_id_rent(rent_id)
        ok = 0
        for rent in self._rentals:
            if str(rent.rental_id) == str(rent_id):
                ok = 1
        if ok == 0:
            raise RepositoryError("This rental does not exist! ")
        else:
            for rent in self._rentals:
                if str(rent.rental_id) == str(rent_id):
                    rent.returned_date = datetime.date.today()
                    for book_id in self._rented_books_ids:
                        if str(rent_id[:4]) == book_id:
                            self._rented_books_ids.remove(book_id)

    def verify_rented(self, book_id: int):
        if book_id in self._rented_books_ids:
            raise InputError("This book is not available! ")

    def available(self, all_books, ok):
        result = []
        if ok == True:
            for book in all_books:
                if str(book.book_id) not in self._rented_books_ids:
                    result.append(book)
        else:
            for book in all_books:
                if str(book.book_id) in self._rented_books_ids:
                    result.append(book)
        return result

    def times_rented_book(self, book):
        nr = 0
        for rent in self._rentals:
            if rent.book_id == book.book_id:
                nr += 1
        return nr

    """def most_rented_books_repo(self, books_list):
        books_list.sort(reverse=True, key=self.times_rented_book)
        return books_list"""

    def most_rented_books_repo(self, books_list):
        # Calculate rented counts for all books
        rented_counts = {book.book_id: self.times_rented_book(book) for book in books_list}

        # Sort the books based on the number of times they are rented
        sorted_books = sorted(books_list, key=lambda book: rented_counts[book.book_id], reverse=True)

        # Create a list of book information, including the number of rentals
        book_counts = []
        for book in sorted_books:
            rented_count = rented_counts[book.book_id]
            book_info = f"{book.title} by {book.author} with ID: {book.book_id} : {rented_count} times rented"
            book_counts.append(book_info)

        return book_counts

    def times_rented_client(self, client):
        nr = 0
        for rent in self._rentals:
            if rent.client_id == client.client_id:
                if rent.returned_date == None:
                    nr += (datetime.date.today() - rent.rented_date).days
                else:
                    nr += (rent.returned_date - rent.rented_date).days
        return nr

    def most_active_clients_repo(self, clients_list):
        # Calculate rented counts for all clients
        rented_counts = {client: self.times_rented_client(client) for client in clients_list}

        # Sort the clients based on the number of times they rented
        sorted_clients = sorted(clients_list, key=lambda client: rented_counts[client], reverse=True)

        # Create a list of client information, including the number of rentals
        client_counts = []
        for client in sorted_clients:
            rentals_count = rented_counts[client]
            client_info = f"{client.name}: {rentals_count} rental days"
            client_counts.append(client_info)

        return client_counts

    def find_return_book(self, book_id, books_list):
        for book in books_list:
            if str(book.book_id) == str(book_id):
                return book.author

    def times_rented_author(self, book, books_list):
        nr = 0
        for rent in self._rentals:
            author = self.find_return_book(rent.book_id, books_list)
            if author == book.author:
                nr += 1
        return nr

    def most_rented_author_repo(self, books_list):
        # Calculate rented counts for all books
        rented_counts = {book: self.times_rented_author(book, books_list) for book in books_list}

        # Sort the books based on the number of times they are rented
        sorted_books = sorted(books_list, key=lambda book: rented_counts[book], reverse=True)

        # Create a set to keep track of unique authors
        unique_authors = set()

        # Create a list of author information, each author only once
        author_counts = []
        for book in sorted_books:
            if book.author not in unique_authors:
                author_info = f"{book.author}: {rented_counts[book]} times rented"
                author_counts.append(author_info)
                unique_authors.add(book.author)

        return author_counts
