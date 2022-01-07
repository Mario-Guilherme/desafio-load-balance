
class User:

    def __init__(self, ttask):
        self.ttask = ttask
    
    @property
    def ttask(self):
        return self.__ttask

    @ttask.setter
    def ttask(self, ttask):
        self.__ttask = ttask
