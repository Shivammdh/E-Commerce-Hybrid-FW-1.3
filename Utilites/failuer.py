import unittest
class FailureException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class TestFail(unittest.TestCase):
    def test_fail(self,msg):
        self.fail(msg)
