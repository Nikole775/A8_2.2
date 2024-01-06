from A8_2_2.UI.ui import Book_services, Book_Repository, UI, Client_Services, Client_Repository, Rental_Repository, Rental_services

if __name__ == '__main__':

    book_repository, client_repository, rent_repository = Book_Repository(), Client_Repository(), Rental_Repository()
    book_services, client_services, rent_services = Book_services(book_repository), Client_Services(client_repository), Rental_services(rent_repository, book_repository, client_repository)
    ui = UI(book_services, client_services, rent_services)
    ui.start()