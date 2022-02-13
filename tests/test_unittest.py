import unittest
from main import multiplicate_int, multiplicate_string


class TestFunctions(unittest.TestCase):
    def test_multiplicate_int(self):
        self.assertEqual(multiplicate_int(2, 3), 6)

    def test_multiplicate_string(self):
        self.assertEqual(multiplicate_string('v', 3), 'vvv')

    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass -- work')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass -- work')

    @unittest.skipIf(multiplicate_int(1, 1), 'Not intereseted')
    def test_multiplicate_int(self):
        self.assertEqual(multiplicate_int(2, 3), 6)


if __name__ == '__main__':
    unittest.main()