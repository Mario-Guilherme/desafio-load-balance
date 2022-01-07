"""File to test."""
from utils.transform_data import transform_data
import unittest


class TesteTransformData(unittest.TestCase):
    """Class to test."""

    def test_transform_data(self):
        """Fuction to test transform data."""
        content = ["6", "4", "5", "7", "0", "2", "1", "0", "0", "0", "8"]
        content_transform = [6, 4, 5, 7, 0, 2, 1, 0, 0, 0, 8]
        self.assertEqual(content_transform, transform_data(content))
