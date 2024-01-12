from A8_2_2.repository.client_repository import Client_Repository
from A8_2_2.services.clients_services import Client_Services
from A8_2_2.domain.validators_exceptions import ClientValidatorException, InputError
from unittest.case import TestCase

import unittest

class TestClientServices(unittest.TestCase):
    def setUp(self):
        self.client_repository = Client_Repository()
        self.client_services = Client_Services(self.client_repository)

    def test_add_client_valid(self):
        # Add a client to the repository for testing
        client_id = "1234"
        name = "Test Client"
        self.client_services.add_client(client_id, name)
        # Ensure the client is added to the repository
        added_client = self.client_services.find_client_id_services(client_id)
        self.assertTrue(added_client)

    def test_add_client_invalid_id(self):
        with self.assertRaises(ClientValidatorException):
            self.client_services.add_client("invalid_id", "Invalid Client")

    def test_add_client_existing_id(self):
        self.client_services.add_client("5678", "Existing Client")
        # Try adding another client with the same ID (should raise an exception)
        with self.assertRaises(ClientValidatorException):
            self.client_services.add_client("5678", "Duplicate Client")

    def test_add_client_empty_name(self):
        with self.assertRaises(ClientValidatorException):
            self.client_services.add_client("9999", "")

    def test_list_clients_with_clients(self):
        # Add a few clients to the repository for testing
        self.client_services.add_client("1234", "Client 1")
        self.client_services.add_client("5678", "Client 2")
        # Ensure that the list_clients method returns the correct list of clients
        expected_result = self.client_repository.get_all_clients()
        result = self.client_services.list_clients()
        self.assertEqual(result, expected_result)

    def test_delete_client_valid(self):
        # Add a client to the repository for testing
        client_id = "1234"
        name = "Test Client"
        self.client_services.add_client(client_id, name)
        # Delete the client using delete_client
        self.client_services.delete_client(client_id)
        # Ensure the client is removed from the repository
        with self.assertRaises(InputError):
            self.client_services.search_client_id_services(client_id)

    def test_delete_client_invalid_id(self):
        # Try deleting a client with an invalid ID (not an integer)
        with self.assertRaises(InputError):
            self.client_services.delete_client("invalid_id")

    def test_delete_client_nonexistent(self):
        # Try deleting a client that does not exist in the repository
        with self.assertRaises(InputError):
            self.client_services.delete_client("9999")

    """def test_update_client_valid(self):
        # Generate a client with a known ID for testing
        client_id = "1234"
        name = "Test Client"
        self.client_services.add_client(client_id, name)

        # Update the client with new details
        new_name = "Updated Client"
        self.client_services.update_client(client_id, new_name)

        # Check if the client with updated information is in the repository
        updated_client_found = self.client_services.search_client_id_services(client_id)

        # Print information for debugging
        print("Updated client found:", updated_client_found)
        print("All clients in repository:", self.client_services.list_clients())

        # Ensure the client with updated information is present
        self.assertTrue(updated_client_found, "Client with updated information not found in repository.")

        # Access client attributes only if it exists
        if updated_client_found:
            # Your existing test logic here
            # For example:
            self.assertEqual(updated_client_found.name, new_name)"""

    def test_update_client_invalid_id(self):
        # Try updating a client with an invalid ID (not a 4-digit number)
        with self.assertRaises(ClientValidatorException):
            self.client_services.update_client("invalid_id", "Updated Client")

    def test_update_client_empty_name(self):
        # Add a client to the repository for testing
        client_id = "5678"
        name = "Test Client"
        self.client_services.add_client(client_id, name)

        # Try updating the client with an empty name (should raise an exception)
        with self.assertRaises(ClientValidatorException):
            self.client_services.update_client(client_id, "")

    if __name__ == "__main__":
        unittest.main()
