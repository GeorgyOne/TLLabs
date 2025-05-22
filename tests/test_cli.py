import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import unittest
from io import StringIO
from contextlib import redirect_stdout

from tllabs import main


class TestCLI(unittest.TestCase):
    def test_default_greeting(self):
        buf = StringIO()
        with redirect_stdout(buf):
            main([])
        self.assertEqual(buf.getvalue().strip(), "Hello from TLLabs")

    def test_custom_greeting(self):
        buf = StringIO()
        with redirect_stdout(buf):
            main(["--greet", "Hi"])
        self.assertEqual(buf.getvalue().strip(), "Hi")


if __name__ == "__main__":
    unittest.main()
