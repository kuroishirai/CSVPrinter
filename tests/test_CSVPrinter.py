import unittest
import os
from speciallecture.CSVPrinter import CSVPrinter

class TestCSVPrinter(unittest.TestCase):
    def test_read_row(self):
        dir_path = os.path.dirname(os.path.abspath(__file__))
        printer = CSVPrinter(os.path.join(dir_path,"sample.csv"))
        l = printer.read()
        self.assertEqual(4,len(l))


    def test_read_col(self):
        dir_path = os.path.dirname(os.path.abspath(__file__))
        printer = CSVPrinter(os.path.join(dir_path,"sample.csv"))
        l = printer.read()
        self.assertEqual(2,len(l[0]))

    def test_read_error(self):
        dir_path = os.path.dirname(os.path.abspath(__file__))
        printer = CSVPrinter(os.path.join(dir_path,"saple.csv"))
        try:
            l = printer.read()
        except FileNotFoundError:
            l = -1
        """
        with self.assertRaises:
            l = -1
        """
        self.assertEqual(-1,l)