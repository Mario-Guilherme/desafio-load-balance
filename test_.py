"""File to run tests."""
from tests.test_utils.test_handle_file import TestReadFile
from tests.test_utils.test_clean_data import CleanData
from tests.test_utils.teste_transform_data import TesteTransformData
from tests.test_server.test_server import TesteServer
from tests.test_loadbalance.teste_loadbalance import TestLoadBalancer
import unittest
from manage import run


def suite():
    """fuction to suite test."""
    suite = unittest.TestSuite()
    suite.addTest(TestReadFile)
    suite.addTest(CleanData)
    suite.addTest(TesteTransformData)
    suite.addTest(TesteServer)
    suite.addTest(TestLoadBalancer)
    return suite


if __name__ == "__main__":
    run()
    unittest.TextTestRunner(verbosity=5).run(suite())
