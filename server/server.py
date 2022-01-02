class Server:

    def __init__(self, id, status, cost):
        self.id = id
        self.status = status
        self.cost = cost
    
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, _status):
        self.__status = _status

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, cost):
        self.__cost = cost


    def create_server(self, umax):
        
        server = {"id":self.id,
                "number_user": 0, 
                "ttask": [],
                "umax": umax,
                "status": self.__status,
                "cost":self.__cost}
        
        return server
    
    @staticmethod
    def allocate_on_server(server, user_ttask):
        server["number_user"] = server["number_user"] +1
        server["ttask"].append(user_ttask)
        return server

    def process_task(self, server):

        ttask = [task -1 for task in  server["ttask"] if task > 0]
        server["number_user"] = len(ttask)
        server['ttask'] = ttask
        self.__cost = self.__cost +1
        server['cost'] = self.__cost
        return server

    def delete_server(self, server):
        self.__status = 0
        server["status"] = self.__status
        return server