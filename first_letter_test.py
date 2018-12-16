import unittest
from first_letter import first_letter

class TestLambda(unittest.TestCase):
    def test_first_letter(self):
        self.assertEqual(first_letter("bananas"), "b")
