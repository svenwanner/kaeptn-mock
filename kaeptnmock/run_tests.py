import unittest
from simple_generators import *


class GeneratorMethods(unittest.TestCase):

    def test_simple_generators(self):
        self.assertEqual(np.count_nonzero(
            unit_sequence_1d(3)-np.array([0.0, 0.5, 1.0])), 0)


if __name__ == '__main__':
    unittest.main()
