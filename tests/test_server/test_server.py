"""File to test."""
from server.server import Server
import unittest


class TesteServer(unittest.TestCase):
    """Class to teste server."""

    def setUp(self):
        """Set up test."""
        self.umax = 4
        self.user_ttask = 3
        self.server = Server(id=0, status=1, cost=0)

    def teste_create_server(self):
        """Fuction to test create_server."""
        server_result = {
            "id": 0,
            "number_user": 0,
            "ttask": [],
            "umax": 4,
            "status": 1,
            "cost": 0,
        }
        self.assertEqual(server_result, self.server.create_server(self.umax))

    def teste_allocate_on_server(self):
        """Teste fuction allocate on server."""
        server_result = {
            "id": 0,
            "number_user": 1,
            "ttask": [3],
            "umax": 4,
            "status": 1,
            "cost": 0,
        }

        server_test = self.server.create_server(self.umax)
        server_test = self.server.allocate_on_server(server_test, self.user_ttask)

        self.assertEqual(server_result, server_test)

    def test_process_task(self):
        """fuction to test process task."""
        server_result = {
            "id": 0,
            "number_user": 1,
            "ttask": [2],
            "umax": 4,
            "status": 1,
            "cost": 1,
        }
        server_test = self.server.create_server(self.umax)
        server_test = self.server.allocate_on_server(server_test, self.user_ttask)
        server_test = self.server.process_task(server_test)

        self.assertEqual(server_result, server_test)

    def test_delete_server(self):
        """Fuction to test delete server."""
        server_result = {
            "id": 0,
            "number_user": 0,
            "ttask": [],
            "umax": 4,
            "status": 0,
            "cost": 3,
        }
        server_test = self.server.create_server(self.umax)
        server_test = self.server.allocate_on_server(server_test, self.user_ttask)
        while server_test["number_user"] != 0:
            server_test = self.server.process_task(server_test)
        server_test = self.server.delete_server(server_test)

        self.assertEqual(server_result, server_test)
