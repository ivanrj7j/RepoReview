import unittest
from src import env

class TestEnvironemnts(unittest.TestCase):
    def test_environemntVariables(self):
        self.assertIsNotNone(env.API_KEY)
        self.assertGreater(len(env.API_KEY), 0)
        self.assertIsNotNone(env.GEMINI_API_KEY)
        self.assertGreater(len(env.GEMINI_API_KEY), 0)