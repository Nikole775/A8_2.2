from A8_2_2.domain.rental import Rental
from A8_2_2.domain.validators_exceptions import RepositoryError, ClientValidator, BookValidator, InputError
import datetime
class Rental_Repository:

    def __init__(self):
        self._rentals = []
        self._rented_books_ids = []

    def add_generated_rentals(self, rental):
        book_id = rental.book_id
        if rental.returned_date is None:
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

    def search_rental(self, rent_id):
        BookValidator.verify_id_rent(rent_id)
        if rent_id not in self._rented_books_ids:
            raise RepositoryError("This rental does not exist! ")
        else:
            for rent in self._rentals:
                if str(rent.rent_id) == str(rent_id):
                    rent.returned_date = datetime.date.today()

    def verify_rented(self, book_id: int):
        if book_id in self._rented_books_ids:
            raise InputError("This book is not available! ")

    def available(self, all_books, ok):
        result = []
        if ok == True:
            for book in all_books:
                if book.book_id not in self._rented_books_ids:
                    result.append(book)
        else:
            for book in all_books:
                if book.book_id in self._rented_books_ids:
                    result.append(book)
        return result
