"""file that works with server."""


class Server:
    """class that handles a server."""

    def __init__(self, id, status, cost):
        """class constructor.

        Keyword arguments:
        id -- unique identifier.
        status --  server status 0(off) and 1(on).
        cost -- server cost.
        """
        self.id = id
        self.status = status
        self.cost = cost

    @property
    def status(self):
        """get status fuction."""
        return self.__status

    @status.setter
    def status(self, _status):
        """set status fuction."""
        self.__status = _status

    @property
    def cost(self):
        """get cost fuction."""
        return self.__cost

    @cost.setter
    def cost(self, cost):
        """set cost fuction."""
        self.__cost = cost

    def create_server(self, umax):
        """create a dictionary.

        Keyword arguments:
        umax -- maximum number of users on a server

        return:
            dict:
                id -- unique identifier.
                number_user -- current number of users.
                ttask -- list of ttask.
                umax -- maximum number of users on a server.
                status -- status server.
                cost -- server cost.
        """
        server = {
            "id": self.id,
            "number_user": 0,
            "ttask": [],
            "umax": umax,
            "status": self.__status,
            "cost": self.__cost,
        }

        return server

    @staticmethod
    def allocate_on_server(server, user_ttask):
        """add ttask in list server.

        Keyword arguments:
        server -- dict.
        user_ttask -- ttask.
        """
        server["number_user"] = server["number_user"] + 1
        server["ttask"].append(user_ttask)
        return server

    def process_task(self, server):
        """process a task.

        Keyword arguments:
        server -- dict.
        """
        ttask = [task - 1 for task in server["ttask"] if task > 1]
        server["number_user"] = len(ttask)
        server["ttask"] = ttask
        self.__cost = self.__cost + 1
        server["cost"] = self.__cost
        return server

    def delete_server(self, server):
        """delete a server.

        Keyword arguments:
        server -- dict.
        """
        self.__status = 0
        server["status"] = self.__status
        return server
