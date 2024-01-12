from A8_2_2.repository.client_repository import Client_Repository, Client
from random import randint, choice
from A8_2_2.domain.validators_exceptions import ClientValidator

class Client_Services:

    def __init__(self, repository):
        self.__repository = repository
        self.generate_n_clients()

    def generate(self):
        # generate client_id
        client_id_used = []
        client_id = randint(1000, 9999)
        while client_id in client_id_used:
            client_id = randint(1000, 9999)
        client_id_used.append(client_id)

        # generate name
        first_name = ["Alex", "Gloria", "Anne", "John", "Thomas", "Amy", "Aaron", "Michel", "Larisa", "David"]
        last_name = ["Pop", "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Lopez", "Davis"]
        name = choice(first_name) + " " + choice(last_name)

        return self.__repository.create_client(client_id, name)

    def generate_n_clients(self):
        for i in range(20):
            self.__repository.add_generated_client(self.generate())

    def list_clients(self):
        """Inputs:
            None
            Retrieves the list of all clients from the repository using the get_all_clients method.
            Outputs:
            Returns a list of all clients in the repository."""
        return self.__repository.get_all_clients()

    def add_client(self, client_id, name):
        """Inputs:
            client_id (string): The ID of the client to be added.
            name (string): The name of the client to be added.
            Validates the client_id using the find_client_id method to ensure it does not already exist.
            Creates a new client object using the create_client method.
            Validates the new client using the ClientValidator.validate_client method.
            Adds the new client to the repository using the add_new_client method.
            Raises a ClientValidatorException if:
                The client_id is not a valid 4-digit number.
                The client_id already exists in the repository.
                The name field is empty."""
        client = self.__repository.create_client(client_id, name)
        ClientValidator.validate_client(client)
        self.__repository.add_new_client(client)

    def delete_client(self, client_id):
        """Inputs:
            client_id (string): The ID of the client to be deleted.
            Validates the client_id using the search_client_id_services method to ensure it exists.
            Removes the client from the repository using the remove_client method.
        Exceptions:
            Raises an InputError if:
            The client_id is not an integer.
            The client with the specified ID does not exist."""
        self.search_client_id_services(client_id)
        self.__repository.remove_client(client_id)

    def update_client(self, client_id, name):
        """Inputs:
            client_id (string): The ID of the client to be updated.
            name (string): The new name for the client.
            Creates a new Client object with the provided client_id and name.
            Validates the new client using the ClientValidator.validate_client method.
            Replaces the existing client in the repository with the new client using the replace_client method.
        Exceptions:
            Raises a ClientValidatorException if:
            The client_id is not a valid 4-digit number.
            The name field is empty."""
        new_client = Client(client_id, name)
        ClientValidator.validate_client(new_client)
        self.__repository.replace_client(new_client)

    def search_client_id_services(self, client_id):
        self.__repository.search_client_id(client_id)

    def search_client_by_id(self, partial):
        return self.__repository.search_client_by_id_repo(partial)

    def search_client_by_name(self, partial):
        return self.__repository.search_client_by_name_repo(partial)

    def find_client_id_services(self, client_id):
        return self.__repository.find_client_id(client_id)