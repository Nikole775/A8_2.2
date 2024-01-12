from A8_2_2.repository.rental_repository import Rental_Repository, Rental
from A8_2_2.repository.client_repository import Client_Repository
from A8_2_2.repository.book_repository import Book_Repository
import random
import datetime


class Rental_services:

    def __init__(self, repository, book_repo, client_repo):
        self.__repository = repository
        self.__book_repo = book_repo
        self.__client_repo = client_repo
        self.generate_n_rentals()


    def generate_rental(self):

        # get book_id
        books_list = self.__book_repo.get_all_books()
        rented_books_id = []
        # get client_id
        clients_list = self.__client_repo.get_all_clients()
        rented_clients_id = []
        # generate rented_id
        book_id = random.choice(books_list).book_id
        while book_id in rented_books_id:
            book_id = random.choice(books_list).book_id
        rented_books_id.append(book_id)

        client_id = random.choice(clients_list).client_id
        while client_id in rented_clients_id:
            client_id = random.choice(clients_list).client_id
        rented_clients_id.append(client_id)

        rented_id = str(book_id) + str(client_id)

        # generate ranted_date and returned date
        rented_date = self.generate_rental_dates()
        # Calculate returned_date as rented_date + 2 weeks
        if datetime.date.today() - rented_date > datetime.timedelta(weeks=2):
            returned_date = rented_date + datetime.timedelta(weeks=2)
            return Rental(rented_id, book_id, client_id, rented_date, returned_date)
        else:
            return Rental(rented_id, book_id, client_id, rented_date)

    def generate_rental_dates(self):
        # Generate a random rented_date within the last year
        start_date = datetime.date.today() - datetime.timedelta(days=365)
        rented_date = self.random_date(start_date)
        return rented_date

    def random_date(self, start_date):
        end_date = datetime.date.today()
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        return random_date

    def generate_n_rentals(self):
        for i in range(20):
            rental = self.generate_rental()
            if rental:
                self.__repository.add_generated_rentals(rental)

    def available_services(self, ok):
        all_books = self.__book_repo.get_all_books()
        return self.__repository.available(all_books, ok)

    def verify_book_id(self, book_id):
        self.__book_repo.search_id(book_id)
        self.__repository.verify_rented(book_id)

    def verify_client(self, client_id):
        return self.__repository.verify_existent_client(client_id)

    def add_rental(self, book_id, client_id):
        rent_id = str(book_id) + str(client_id)
        rented_date = datetime.date.today()
        self.__repository.add_new_rental(rent_id, book_id, client_id, rented_date)

    def display_rentals(self):
        return self.__repository.get_all_rentals()

    def search_rental_id(self, rent_id):
        self.__repository.search_rental(rent_id)

    def most_rented_books(self):
        books_list = self.__book_repo.get_all_books()
        return (self.__repository.most_rented_books_repo(books_list))

    def most_active_clients(self):
        clients_list = self.__client_repo.get_all_clients()
        return(self.__repository.most_active_clients_repo(clients_list))

    def most_rented_author(self):
        books_list = self.__book_repo.get_all_books()
        return self.__repository.most_rented_author_repo(books_list)
