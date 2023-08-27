import unittest
from string import Formatter

class poc_formatter(unittest.TestCase):
    def test_poc_formatter_1(self):
        yourstring = "sadfhfjwopf {fad}asdasd{asd}"
        names = [fn for _, fn, _, _ in Formatter().parse(yourstring) if fn is not None]
        
        self.assertEqual(names, ['fad', 'asd'])
