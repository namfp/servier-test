import unittest

from sparse_array import SparseArray


class TestSum(unittest.TestCase):
    def test_1(self):
        sparse_array = SparseArray(["aba", "baba", "aba", "xzxb"])
        result = sparse_array.compute(["aba", "xzxb", "ab"])
        self.assertEqual(result["aba"], 2)
        self.assertEqual(result["xzxb"], 1)
        self.assertEqual(result["ab"], 0)

    def test_2(self):
        sparse_array = SparseArray(["def", "de", "fgh"])
        result = sparse_array.compute(["de", "lmn", "fgh"])
        self.assertEqual(result["de"], 1)
        self.assertEqual(result["lmn"], 0)
        self.assertEqual(result["fgh"], 1)


if __name__ == '__main__':
    unittest.main()