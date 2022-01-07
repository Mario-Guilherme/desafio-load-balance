"""File to test fuction handle file."""
from utils.handle_file import ReadFile
from manage import dict_config

import unittest


class TestReadFile(unittest.TestCase):
    """Class to test."""

    def test_file_content(self):
        """Test file_content."""
        content = [
            "6\n",
            "4\n",
            "5\n",
            "7\n",
            "0\n",
            "2\n",
            "1\n",
            "0\n",
            "0\n",
            "0\n",
            "8",
        ]
        content_file = ReadFile().list_content()

        self.assertEqual(content, content_file)
