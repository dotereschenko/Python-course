import unittest
from complex import Complex

class TestComplex(unittest.TestCase):
    def test_add(self):
        first = Complex(1, 2)
        second = Complex(2, 1)
        self.assertEqual(first.add(second), Complex(3, 3))

    def test_sub(self):
        first = Complex(3, 1)
        second = Complex(1, 2)
        ans = Complex(2, -1)
        self.assertEqual(first.sub(second), ans)

    def test_mul(self):
        first = Complex(1, 3)
        second = Complex(2, -2)
        self.assertEqual(first.mul(second), Complex(8, 4))

    def test_div(self):
        first = Complex(4, 5)
        second = Complex(0, 1)
        ans = Complex(5, -4)
        self.assertEqual(first.div(second), ans)

    def test_sub_null_im(self):
        first = Complex(3, 2)
        second = Complex(4, 0)
        self.assertEqual(first.sub(second), Complex(-1, 2))

    def test_add_null_im(self):
        first = Complex(1, 0)
        second = Complex(2, 1)
        self.assertEqual(first.add(second), Complex(3, 1))

    def test_abs(self):
        c = Complex(3, 4)
        self.assertEqual(c.abs(), 5)

if __name__ == "__main__":
    unittest.main()
