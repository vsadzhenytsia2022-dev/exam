import unittest
from main import validate_email

class TestFunction(unittest.TestCase):
    def test_my_function(self):
        # Перевірка валідного email
        self.assertTrue(validate_email("user@mail.com"))
        # Перевірка невалідного email (без крапки після @)
        self.assertFalse(validate_email("user@com"))
        # Перевірка невалідного email (без @)
        self.assertFalse(validate_email("myemail.com"))

if __name__ == "__main__":
    unittest.main()