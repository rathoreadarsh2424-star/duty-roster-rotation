import unittest
from main import rotateRoster


class TestRotateRoster(unittest.TestCase):
    def test_sample_one(self):
        self.assertEqual(rotateRoster(["A", "B", "C", "D", "E"], 2),
                         ["D", "E", "A", "B", "C"])

    def test_sample_two_large_k(self):
        self.assertEqual(rotateRoster(["A", "B", "C", "D", "E"], 7),
                         ["D", "E", "A", "B", "C"])

    def test_zero_rotation(self):
        self.assertEqual(rotateRoster(["A", "B", "C"], 0), ["A", "B", "C"])

    def test_full_rotation(self):
        self.assertEqual(rotateRoster(["A", "B", "C"], 3), ["A", "B", "C"])

    def test_single_name(self):
        self.assertEqual(rotateRoster(["A"], 10**9), ["A"])


if __name__ == "__main__":
    unittest.main()
