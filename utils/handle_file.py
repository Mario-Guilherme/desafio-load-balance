import os
import glob
from manage import dict_config

class ReadFile(object):
    
    def __init__(self):
        super().__init__()
        pass
    
    @staticmethod
    def read_file_input():
        file = open(dict_config["INPUT_FILE"], "r")
        return file

    @staticmethod
    def close_file(file):
        file.close()

    def list_content(self):
        open_file = self.read_file_input()
        content_file = open_file.readlines()
        self.close_file(open_file)
        return content_file

    
    

class WriteFile(object):

    def __init__(self):
        super().__init__()
        pass
       
    @staticmethod
    def write_file_output():

        file = open(dict_config["OUTPUT_FILE"], "w")

        return file

#ReadFile("files").read_files()


