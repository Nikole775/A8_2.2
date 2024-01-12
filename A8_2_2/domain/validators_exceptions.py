class InputError(Exception):
    pass


class UIerror(Exception):
    pass


class RepositoryError(Exception):
    pass


class BookValidatorException(Exception):
    pass


class BookValidator:
    @staticmethod
    def validate_book(book):
        # book = (ISBN, Title, Author)
        if not book.book_id.isdigit() or len(str(book.book_id)) != 4:
            raise BookValidatorException("That was not a valid ID!")
        if book.title == '':
            raise BookValidatorException("Title field cannot be empty!")
        if book.author == '':
            raise BookValidatorException("Author field cannot be empty!")

    @staticmethod
    def verify_id_rent(rent_id):
        if not rent_id.isdigit() or len(str(rent_id)) != 8:
            raise RepositoryError("That was not a valid ID!")


class ClientValidatorException(Exception):
    pass


class ClientValidator:

    @staticmethod
    def validate_client(client):
        if not client.client_id.isdigit() or len(str(client.client_id)) != 4:
            raise ClientValidatorException("Thay was not a valid ID!")
        if client.name == '':
            raise ClientValidatorException("Name field cannot be empty!")

    @staticmethod
    def verify_data(id_):
        if not id_.isdigit() or len(str(id_)) != 4:
            raise InputError("That was not a valid ID!")
