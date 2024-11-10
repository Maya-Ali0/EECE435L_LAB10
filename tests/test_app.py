import unittest
from app import greet
class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("World from Maya Ali"), "Hello, World from Maya Ali!")


if __name__ == "__main__":
    unittest.main()