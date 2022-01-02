from utils.handle_file import ReadFile

import unittest

class TestReadFile(unittest.TestCase):


    def test_read_file(self):
        path = "files"
        files = ReadFile(path).read_files()
        for file in files:
            self.assertEqual()


    pass