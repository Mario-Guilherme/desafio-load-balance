"""file to handle file."""
from manage import dict_config


class ReadFile(object):
    """Class to read file."""

    def __init__(self):
        """Construct."""
        super().__init__()
        pass

    @staticmethod
    def read_file_input():
        """Fuction to read file."""
        file = open(dict_config["INPUT_FILE"], "r")
        return file

    @staticmethod
    def close_file(file):
        """Fuction to close file."""
        file.close()

    def list_content(self):
        """Fuction to show content of file.

        Return:
        list of str.
        """
        open_file = self.read_file_input()
        content_file = open_file.readlines()
        self.close_file(open_file)
        return content_file


class WriteFile(object):
    """Class to write file output."""

    def __init__(self):
        """Construct."""
        super().__init__()
        pass

    @staticmethod
    def create_file_output():
        """Fuction to open file."""
        file = open(dict_config["OUTPUT_FILE"], "a")

        return file

    def write_file_users(self, users):
        """fuction write user in file.

        Keyword arguments:
        users -- list os users
        """
        file = self.create_file_output()
        tick_data = str(users[0])
        for x in users[1:]:
            tick_data = tick_data + "," + str(x)
        tick_data = tick_data + "\n"
        file.writelines(tick_data)

    def write_file_cost(self, cost):
        """Fuction to write cost in file.

        Keyword arguments:
        cost -- cost of server.
        """
        file = self.create_file_output()
        file.writelines(f"{cost}")
