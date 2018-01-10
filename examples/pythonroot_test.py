import pythonroot
import unittest

class TestPythonRoot(unittest.TestCase):
    def test_import(self):
        self.assertIn('pythonroot', pythonroot.pythonroot())
