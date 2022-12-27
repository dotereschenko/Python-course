import unittest
from salary import Paid
import json
import salary

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.salary = Paid()

    def test_get(self):
        a = self.salary.get({"year": 2016, "month": "JULY", "salary": 1000000})
        self.assertTrue(a)

    def test_write(self):
        a = self.salary.get({"year": 2016, "month": "JULY", "salary": 1000000})
        to = "output.json"
        self.assertIsNotNone(salary.write(a,to))

