"""File to test."""
from utils.clean_data import clean_data
import unittest


class CleanData(unittest.TestCase):
    """Class to test."""

    def teste_clean_data(self):
        """Fuction to teste clean data."""
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

        content_clean = ["6", "4", "5", "7", "0", "2", "1", "0", "0", "0", "8"]

        self.assertEqual(content_clean, clean_data(content))
