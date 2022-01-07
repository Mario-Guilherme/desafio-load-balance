"""file to use load balance."""
from server.server import Server
from user.user import User
from utils.handle_file import WriteFile


class LoadBalancer:
    """Class to use Load Blancer."""

    def __init__(self, umax, user_list):
        """Construct load balancer."""
        self._umax = umax
        self._users = user_list
        self._deactive_servers = []
        self._dict_server = {}
        self.id = 0

    @property
    def id(self):
        """get id."""
        return self.__id

    @id.setter
    def id(self, _id):
        """set id."""
        self.__id = _id

    def balancer(self, ttask):
        """load balance servers by allocating users.

        Keyword arguments:
        ttask -- number of tickets for a task .
        """
        file = WriteFile()
        for ttask_user in self._users:

            for i in range(ttask_user):

                id_max = self.find_id_max_value_tttask()
                user = User(ttask)

                if id_max != -1:
                    self.update_user_in_server(id_max, user, self._dict_server)
                else:
                    self._dict_server = self.add_server_in_list(self._dict_server, user)

            self.write_users(file)

            self._dict_server = self.servers_processed_task(self._dict_server)
            self._dict_server = self.update_activite_servers(self._dict_server)

        while self._dict_server != {}:
            self.write_users(file)

            self._dict_server = self.servers_processed_task(self._dict_server)
            self._dict_server = self.update_activite_servers(self._dict_server)

        self.write_cost(file)

    def find_id_max_value_tttask(self):
        """find id with max value in ttask.

        return:
        id with max value.
        """
        max_value_task = -1
        id_max = -1
        for id, data_server in self._dict_server.items():
            if data_server["ttask"] == []:
                value = 0
            else:
                value = max(data_server["ttask"])

            if (
                max_value_task <= value
                and data_server["number_user"] < data_server["umax"]
            ):
                id_max = id
                max_value_task = value
        return id_max

    @staticmethod
    def empty_servers(list_servers):
        """check if the server list is empty."""
        return list_servers != {}

    def update_user_in_server(self, id_max, user, list_servers):
        """allocate user in server.

        Keyword arguments:
        id_max -- id with max value in ttask.
        user -- user
        list_servers -- servers' list

        Return:
        lista of servers with new users
        """
        server_id = list_servers[id_max]
        server = Server(server_id["id"], server_id["status"], server_id["cost"])

        list_servers[id_max] = server.allocate_on_server(server_id, user.ttask)
        return list_servers

    def add_server_in_list(self, list_server, user):
        """add new server in servers' list.

        Keyword arguments:
        list_server -- servers' list.
        user -- user.
        Return:
        servers' list with new server.
        """
        self.id = self.id + 1
        server = Server(id=self.id, status=1, cost=0)
        server_id = server.create_server(self._umax)
        list_server.update({self.id: server_id})
        list_server[self.id] = server.allocate_on_server(server_id, user.ttask)
        return list_server

    def servers_processed_task(self, list_server):
        """get the servers with the tasks processed.

        Return:
        server list with tasks processed.
        """
        for id, server in list_server.items():
            _server = Server(
                id=server["id"], status=server["status"], cost=server["cost"]
            )
            if server["status"] == 1:
                server_process = _server.process_task(server=server)
                list_server[id] = server_process

            if server_process["number_user"] == 0:
                delete_server = _server.delete_server(server=server)
                list_server[id] = delete_server
                self._deactive_servers.append(server)

        return list_server

    def update_activite_servers(self, list_server):
        """update the servers' list  with active servers.

        Return:
        servers' list actives.
        """
        activite_servers = {}
        for id, server in list_server.items():
            if server["status"] == 1:
                activite_servers.update({id: server})

        return activite_servers

    def total_cost_servers(self):
        """total cost of servers.

        Return:
        total cost of servers.
        """
        cost = 0
        for k in self._deactive_servers:
            cost = cost + k["cost"]
        return cost

    def write_users(self, file):
        """writ users in file output.txt."""
        list_users = self.current_users()
        file.write_file_users(list_users)

    def write_cost(self, file):
        """write cost in file output.txt."""
        file.write_file_cost(self.total_cost_servers())

    def current_users(self):
        """create a list of users.

        Return:
        list of users.
        """
        users = [v["number_user"] for v in self._dict_server.values()]

        return users
