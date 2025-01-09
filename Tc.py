#import sys
#import os
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))



import unittest
from src.validator import validate_email_payload

class ValidatorTest(unittest.TestCase):
    def test_valid_payload(self):
        sender_name = "Marketing @ T-Shoes"
        sender_addr = "marketing@tshoes.com"
        receiver_name = "Jane Doe"
        receiver_addr = "janedoe5511@gmail.com"
        html = """
        <!DOCTYPE html>
        <html>
        <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>T-Shoes Discounts!</title>
        </head>
        <body>
        <p>Hi {first_name},</p>
        <p>Marketing message...</p>
        </body>
        </html>
        """
        replacements = {"first_name": "Jane"}
        self.assertTrue(validate_email_payload(sender_name, sender_addr, receiver_name, receiver_addr, html, replacements))

    def test_invalid_sender_name(self):
        sender_name = "A"
        sender_addr = "marketing@tshoes.com"
        receiver_name = "Jane Doe"
        receiver_addr = "janedoe5511@gmail.com"
        html = """
        <!DOCTYPE html>
        <html>
        <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>T-Shoes Discounts!</title>
        </head>
        <body>
        <p>Hi {first_name},</p>
        <p>Marketing message...</p>
        </body>
        </html>
        """
        replacements = {"first_name": "Jane"}
        with self.assertRaises(ValueError):
            validate_email_payload(sender_name, sender_addr, receiver_name, receiver_addr, html, replacements)

    def test_missing_placeholder_in_replacements(self):
        sender_name = "Marketing @ T-Shoes"
        sender_addr = "marketing@tshoes.com"
        receiver_name = "Jane Doe"
        receiver_addr = "janedoe5511@gmail.com"
        html = """
        <!DOCTYPE html>
        <html>
        <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>T-Shoes Discounts!</title>
        </head>
        <body>
        <p>Hi {first_name},</p>
        <p>Marketing message...</p>
        </body>
        </html>
        """
        replacements = {}  # Missing first_name
        with self.assertRaises(ValueError):
            validate_email_payload(sender_name, sender_addr, receiver_name, receiver_addr, html, replacements)

    def test_invalid_email_address(self):
        sender_name = "Marketing @ T-Shoes"
        sender_addr = "invalid-email@com"
        receiver_name = "Jane Doe"
        receiver_addr = "janedoe5511@gmail.com"
        html = """
        <!DOCTYPE html>
        <html>
        <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>T-Shoes Discounts!</title>
        </head>
        <body>
        <p>Hi {first_name},</p>
        <p>Marketing message...</p>
        </body>
        </html>
        """
        replacements = {"first_name": "Jane"}
        with self.assertRaises(ValueError):
            validate_email_payload(sender_name, sender_addr, receiver_name, receiver_addr, html, replacements)

if __name__ == "__main__":
    unittest.main()
