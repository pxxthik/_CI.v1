import unittest
import app

class TestApp(unittest.TestCase):

    def test_add(self):
        self.assertEqual(app.add(1, 2), 3)
        self.assertEqual(app.add(-1, -3), -4)
    
    def test_subtract(self):
        self.assertEqual(app.subtract(1, 2), -1)
        self.assertEqual(app.subtract(-1, -3), 2)
    
    def test_multiply(self):
        self.assertEqual(app.multiply(1, 2), 2)
        self.assertEqual(app.multiply(-1, -3), 3)
    
    def test_divide(self):
        self.assertEqual(app.divide(1, 2), 0.5)
        self.assertEqual(app.divide(-1, -3), 0.3333333333333333)
