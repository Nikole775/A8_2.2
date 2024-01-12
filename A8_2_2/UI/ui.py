from A8_2_2.services.book_services import Book_services, Book_Repository
from A8_2_2.services.clients_services import Client_Services, Client_Repository
from A8_2_2.domain.validators_exceptions import UIerror, BookValidatorException, InputError, ClientValidatorException, RepositoryError
from A8_2_2.services.rental_services import Rental_Repository, Rental_services
class UI:
    def __init__(self, book_services, client_services, rental_services):
        self.__book_services = book_services
        self.__client_services = client_services
        self.__rental_services = rental_services
        self.exit_flag = False
        self.menu_level = 0

    def menu(self):
        print("_________________________________________________________________")
        print("1.Manage clients and books.")
        print("2.Rent or return a book.")
        print("3.Search for clients or books ")
        print("4.Statistics")
        print("0.exit")
        print("_________________________________________________________________")

    def manage_clients_books_menu(self):
        print(".................................................................")
        print("1. add a book")
        print("2.remove a book")
        print("3.update a book")
        print("4.list all the books")
        print("5.add a client")
        print("6.remove a client")
        print("7.update a client")
        print("8.list all clients")
        print("0.back")
        print(".................................................................")

    def rent_return_book_menu(self):
        print(".................................................................")
        print("1.list available books")
        print("2.list books that has to be returned")
        print("3.rent a book")
        print("4.return a book")
        print("0.back")
        print(".................................................................")

    def search_clients_books_menu(self):
        print(".................................................................")
        print("1.search a book by id")
        print("2. search a book by title")
        print("3.search a book by author")
        print("4.search a client by id")
        print("5.search a client by name")
        print("0.back")
        print(".................................................................")

    def statistics_menu(self):
        print(".................................................................")
        print("1.most rented books")
        print("2.most active clients")
        print("3.most rented author")
        print("0.back")
        print(".................................................................")

    def get_input (self, txt="->"):
        return input(txt)

    def choose_option_menu(self,option):
        if option == "1":
            self.menu_level = 1
            self.manage_clients_books()
        elif option == "2":
            self.menu_level = 1
            self.rent_return_book()
        elif option == "3":
            self.menu_level = 1
            self.search_clients_books()
        elif option == "4":
            self.menu_level = 1
            self.statistics()
        elif option == "0":
            print("You stopped the program. Bye!")
            self.exit_flag = True
        else:
            raise UIerror("That was not a valid option!")

    def manage_clients_books(self):
        while self.menu_level == 1 :
            try:
                self.manage_clients_books_menu()
                option1 = self.get_input()
                self.choose_option_clients_books(option1)
            except UIerror as ve:
                print(ve)

    def rent_return_book(self):
        while self.menu_level == 1:
            try:
                self.rent_return_book_menu()
                option2 = self.get_input()
                self.choose_option_rent_return_book(option2)
            except UIerror as ve:
                print(ve)

    def search_clients_books(self):
        while self.menu_level == 1:
            try:
                self.search_clients_books_menu()
                option3 = self.get_input()
                self.choose_option_search_clients_books(option3)
            except UIerror as ve:
                print(ve)

    def statistics(self):
        while self.menu_level == 1:
            try:
                self.statistics_menu()
                option4 = self.get_input()
                self.choose_option_statistics(option4)
            except UIerror as ve:
                print(ve)

    def choose_option_clients_books(self,option):
        if option == "1":
            self.add_book_UI()
        elif option == "2":
            self.remoove_book_UI()
        elif option == "3":
            self.update_book_UI()
        elif option == "4":
            self.list_books_UI()
        elif option == "5":
            self.add_client_UI()
        elif option == "6":
            self.remove_client_UI()
        elif option == "7":
            self.update_client_UI()
        elif option == "8":
            self.list_clients_UI()
        elif option == "0":
            self.menu_level = 0
        else:
            raise UIerror("That was not a valid option!")

    def choose_option_rent_return_book(self, option):
        if option == "1":
            self.list_available_UI()
        elif option == "2":
            self.list_rented_UI()
        elif option == "3":
            self.rent_book_UI()
        elif option == "4":
            self.return_book_UI()
        elif option == "9":
            self.list_rentals()
        elif option == "0":
            self.menu_level = 0
        else:
            raise UIerror("That was not a valid option!")

    def choose_option_search_clients_books(self, option):
        if option == "1":
            self.search_book_client_id(option)
        elif option == "2":
            self.search_book_client_by_string(option)
        elif option == "3":
            self.search_book_client_by_string(option)
        elif option == "4":
            self.search_book_client_id(option)
        elif option == "5":
            self.search_book_client_by_string(option)
        elif option == "0":
            self.menu_level = 0
        else:
            raise UIerror("That was not a valid option! ")

    def choose_option_statistics(self, option):
        if option == "1":
            self.most_rented_books_UI()
        elif option == "2":
            self.most_active_clients_UI()
        elif option == "3":
            self.most_rented_author_UI()
        elif option == "0":
            self.menu_level = 0
        else:
            raise UIerror("That was not a valid option!")

    def list_books_UI(self):
        print(self.__book_services.list_books())

    def add_book_UI(self):
        try:
            book_id = self.get_input("Book ID: ")
            title = self.get_input("Title: ")
            author = self.get_input("Author: ")
            self.__book_services.add_book(book_id, title, author)
        except BookValidatorException as ve:
            print(ve)

    def remoove_book_UI(self):
        try:
            book_id = self.get_input("Book ID: ")
            self.__book_services.delete_book(book_id)
        except InputError as ve:
            print(ve)

    def update_book_UI(self):
        try:
            book_id = self.get_input("Book ID: ")
            self.__book_services.search_id_services(book_id)
            try:
                title = self.get_input("New Title: ")
                author = self.get_input("New Author: ")
                self.__book_services.update_book(book_id, title, author)
            except BookValidatorException as ve:
                print(ve)
        except InputError as ve:
            print(ve)

    def list_clients_UI(self):
        print(self.__client_services.list_clients())

    def add_client_UI(self):
        try:
            client_id = self.get_input("Client ID: ")
            name = self.get_input("Name: ")
            self.__client_services.add_client(client_id, name)
        except ClientValidatorException as ve:
            print(ve)

    def remove_client_UI(self):
        try:
            client_id = self.get_input("Client ID: ")
            self.__client_services.delete_client(client_id)
        except InputError as ve:
            print(ve)

    def update_client_UI(self):
        try:
            client_id = self.get_input("Client ID: ")
            self.__client_services.search_client_id_services(client_id)
            try:
                name = self.get_input("New Name: ")
                self.__client_services.update_client(client_id, name)
            except ClientValidatorException as ve:
                print(ve)
        except InputError as ve:
            print(ve)

    def list_available_UI(self):
        print(self.__rental_services.available_services(True))

    def list_rented_UI(self):
        print(self.__rental_services.available_services(False))

    def rent_book_UI(self):
        try:
            book_id = self.get_input("Book Id:")
            self.__rental_services.verify_book_id(book_id)
            client_id = self.get_input("Client ID: ")
            try:
                if self.__rental_services.verify_client(client_id) == True:
                    self.__rental_services.add_rental(book_id, client_id)
                else:
                    name = self.get_input("Give the name of the new client: ")
                    self.__client_services.add_client(client_id, name)
                    self.__rental_services.add_rental(book_id, client_id)
            except InputError as ve:
                print(ve)
        except InputError as ve:
            print(ve)

    def return_book_UI(self):
        try:
            rent_id = self.get_input("Give the rental ID: ")
            self.__rental_services.search_rental_id(rent_id)
        except RepositoryError as ve:
            print(ve)

    def list_rentals(self):
        print(self.__rental_services.display_rentals())

    def search_book_client_id(self, option):
        try:
            if option == "1":
                partial_id = self.get_input("Give the wanted ID: ")
                print(self.__book_services.search_book_by_id(partial_id))
            else:
                partial_id = self.get_input("Give the wanted ID: ")
                print(self.__client_services.search_client_by_id(partial_id))
        except InputError as ve:
            print(ve)

    def search_book_client_by_string(self, option):
        try:
            if option == "2":
                partial_title = self.get_input("Give the wanted Title: ")
                print(self.__book_services.search_book_by_title(partial_title))
            elif option == "3":
                partial_author = self.get_input("Give the wanted Author: ")
                print(self.__book_services.search_book_by_author(partial_author))
            else:
                partial_name = self.get_input("Give the wanted Name: ")
                print(self.__client_services.search_client_by_name(partial_name))
        except InputError as ve:
            print(ve)

    def most_rented_books_UI(self):
        print(*self.__rental_services.most_rented_books(), sep='\n')

    def most_active_clients_UI(self):
        print(*self.__rental_services.most_active_clients(), sep='\n')

    def most_rented_author_UI(self):
        print(*self.__rental_services.most_rented_author(), sep='\n')

    def start(self):
        while not self.exit_flag:
            try:
                self.menu()
                option = self.get_input()
                self.choose_option_menu(option)
            except UIerror as ve:
                print(ve)



