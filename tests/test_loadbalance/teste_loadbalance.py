"""File to test."""
from loadbalance.loadbalancer import LoadBalancer
from user.user import User
from manage import dict_config
from utils.transform_data import transform_data

import os

import unittest


class TestLoadBalancer(unittest.TestCase):
    """Class to test LoadBalancer."""

    def setUp(self):
        """Fuction to setup test."""
        self.umax = 4
        self.ttask = 6
        user_list = [5, 7, 0, 2, 1, 0, 0, 0, 8]
        self.user = User(self.ttask)
        self.loadbalance = LoadBalancer(self.umax, user_list)
        pass

    def test_find_id_max_value_ttask_void(self):
        """Fuction to test id max with max value in ttask."""
        id_max = -1

        self.assertEqual(id_max, self.loadbalance.find_id_max_value_tttask())

    def test_add_server_in_list(self):
        """Fuction to test add server in list."""
        result_list_server = {
            1: {
                "id": 1,
                "number_user": 1,
                "ttask": [6],
                "umax": 4,
                "status": 1,
                "cost": 0,
            }
        }

        self.assertEqual(
            result_list_server, self.loadbalance.add_server_in_list({}, self.user)
        )

    def test_empty_servers_false(self):
        """Fuction to test empty server with value false."""
        server_test = {}
        self.assertFalse(self.loadbalance.empty_servers(server_test))

    def test_empty_servers_true(self):
        """Fuction to test empty server with value true."""
        result_list_server = {
            1: {
                "id": 1,
                "number_user": 2,
                "ttask": [6, 6],
                "umax": 4,
                "status": 1,
                "cost": 0,
            }
        }
        self.assertTrue(self.loadbalance.empty_servers(result_list_server))

    def test_update_user_in_server(self):
        """Fuction to test update user in server."""
        result_list_server = {
            1: {
                "id": 1,
                "number_user": 2,
                "ttask": [6, 6],
                "umax": 4,
                "status": 1,
                "cost": 0,
            }
        }
        list_server = {
            1: {
                "id": 1,
                "number_user": 1,
                "ttask": [6],
                "umax": 4,
                "status": 1,
                "cost": 0,
            }
        }
        id_max = 1
        self.assertEqual(
            result_list_server,
            self.loadbalance.update_user_in_server(id_max, self.user, list_server),
        )

    def test_servers_processed_task_status_true(self):
        """Fuction to test server processed ttask status equal 1."""
        result_list_server = {
            1: {
                "id": 1,
                "number_user": 2,
                "ttask": [5, 5],
                "umax": 4,
                "status": 1,
                "cost": 1,
            }
        }
        test_list_server = {
            1: {
                "id": 1,
                "number_user": 2,
                "ttask": [6, 6],
                "umax": 4,
                "status": 1,
                "cost": 0,
            }
        }
        self.assertEqual(
            result_list_server,
            self.loadbalance.servers_processed_task(test_list_server),
        )

    def test_servers_processed_task_number_user_true(self):
        """Fuction to test server processed ttask number user  equal 0."""
        result_list_server = {
            1: {
                "id": 1,
                "number_user": 0,
                "ttask": [],
                "umax": 4,
                "status": 0,
                "cost": 2,
            }
        }
        test_list_server = {
            1: {
                "id": 1,
                "number_user": 3,
                "ttask": [1, 1, 1],
                "umax": 4,
                "status": 1,
                "cost": 1,
            }
        }
        self.assertEqual(
            result_list_server,
            self.loadbalance.servers_processed_task(test_list_server),
        )

    def test_update_activite_servers(self):
        """Fuction to teste update activite servers."""
        result_list_server = {}
        test_list_server = {
            1: {
                "id": 1,
                "number_user": 0,
                "ttask": [],
                "umax": 4,
                "status": 0,
                "cost": 2,
            },
            2: {
                "id": 2,
                "number_user": 0,
                "ttask": [],
                "umax": 4,
                "status": 0,
                "cost": 2,
            },
        }
        self.assertEqual(
            result_list_server,
            self.loadbalance.update_activite_servers(test_list_server),
        )

    def test_balancer(self):
        """fuction to test balancer."""
        result_balancer = [
            [4, 1],
            [4, 4, 4],
            [4, 4, 4],
            [4, 4, 4, 2],
            [4, 4, 4, 3],
            [4, 4, 4, 3],
            [3, 4, 3],
            [3],
            [
                4,
                4,
                3,
            ],
            [2, 4, 3],
            [1, 4, 3],
            [1, 4, 3],
            [1, 4, 3],
            [1, 4, 3],
            [42],
        ]

        if os.path.exists(dict_config["OUTPUT_FILE"]):
            os.remove(dict_config["OUTPUT_FILE"])
        self.loadbalance.balancer(self.ttask)
        file = open(dict_config["OUTPUT_FILE"], "r")
        test_output = []
        for line in file.readlines():
            line = line.split("\n")[0]
            test_output.append(transform_data(line.split(",")))
        file.close()
        self.assertEqual(result_balancer, test_output)
        pass
