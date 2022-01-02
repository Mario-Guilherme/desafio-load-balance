from server.server import Server
from user.user import User


class LoadBalancer:

    def __init__(self, umax, user_list):
        self._umax = umax
        self._users = user_list
        self._deactive_servers = []
        self._dict_server = {}
    

    def balancer(self, ttask):

        for ttask_user  in self._users:

            for one_user in range(ttask_user):

                if self._dict_server == {}:
                    server = Server(id=0, status=1, cost=0)
                    self._dict_server.update({"0": server.create_server(self._umax)})
                else:
                    max_value_task = 0
                    id_max = -1
                    for id, data_server in self._dict_server.items():
                        if data_server["ttask"] == []:
                            value = 0
                        else:
                            value = max(data_server["ttask"])
        
                        if max_value_task <= value and data_server["number_user"] < data_server["umax"]:
                            id_max  =  id
                            max_value_task  = value
                    user = User(ttask)
                    if id_max != -1:
                        server_id =  self._dict_server[f"{id_max}"]
                        server = Server(server_id["id"], server_id["status"], server_id["cost"])
                        
                        self._dict_server[f"{id_max}"] = server.allocate_on_server(server_id, user.ttask)
                    else:
                        id = len(self._dict_server)
                        server = Server(id=id, status=1, cost=0)
                        server_id = server.create_server(self._umax)
                        self._dict_server.update({f"{id}": server_id})
                        server.allocate_on_server(server_id, user.ttask)
                        self._dict_server[f"{id}"] = server.allocate_on_server(server_id, user.ttask)
            
            for key, value in self._dict_server.items():
                
                print(value["number_user"], end=",")

            for id, server in self._dict_server.items():
                _server = Server(id=server["id"], status=server["status"], cost=server["cost"])
                if server["status"] ==1:
                    server_process = _server.process_task(server=server)
                    self._dict_server[f"{id}"] = server_process
                    print(server_process) 


                if server_process["number_user"]==0:
                    delete_server =  _server.delete_server(server=server)
                    self._dict_server[f"{id}"] = delete_server
                    self._deactive_servers.append(server)
                    #self._dict_server.pop(id)
    
                    
            self._dict_server = {f"{id}":server for id, server in  self._dict_server.items() if server["status"]==1}

        while self._dict_server != {}:
            
            for id, server in self._dict_server.items():
                _server = Server(id=server["id"], status=server["status"], cost=server["cost"])
                if server["status"]==1:
                    server_process = _server.process_task(server=server)
                    self._dict_server[f"{id}"] = server_process
                    print(server_process)

                if server_process["number_user"]==0:
                    delete_server =  _server.delete_server(server=server)
                    self._dict_server[f"{id}"] = delete_server
                    self._deactive_servers.append(server)
                    #self._dict_server.pop(id)
    
            self._dict_server = {f"{id}":server for id, server in  self._dict_server.items() if server["status"]==1}
                
                  

                                                
    #def locate_user

#lista_dados = ['4', '2', '1', '3', '0', '1', '0',  '1']
#value = list(map(int, lista_dados))

