import io
import json
import unittest
from contextlib import redirect_stdout
from your_module_name import handle_user_input

class TestHandleUserInput(unittest.TestCase):

    def test_returns_dict(self):
        result = handle_user_input("example")
        self.assertIsInstance(result, dict)
        self.assertEqual(result, {"demo": "safe"})

    def test_printed_output(self):
        f = io.StringIO()
        with redirect_stdout(f):
            handle_user_input("example")

        output = f.getvalue()
        self.assertIn("Would run: echo example", output)
        self.assertIn(
            "Would query: SELECT * FROM users WHERE name = 'example'",
            output,
        )

if __name__ == "__main__":
    unittest.main()
