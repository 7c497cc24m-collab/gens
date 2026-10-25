import unittest

import luhn


class TestLuhn(unittest.TestCase):
    def test_check_digit(self):
        self.assertEqual(luhn.check_digit("7992739871"), 3)
        self.assertEqual(luhn.check_digit("0"), 0)

    def test_is_valid(self):
        self.assertTrue(luhn.is_valid("79927398713"))
        self.assertTrue(luhn.is_valid("4111 1111 1111 1111"))
        self.assertFalse(luhn.is_valid("79927398710"))
        self.assertFalse(luhn.is_valid("abc"))
        self.assertFalse(luhn.is_valid("5"))

    def test_generate(self):
        for length in (2, 11, 16, 19):
            n = luhn.generate("4", length)
            self.assertEqual(len(n), length)
            self.assertTrue(n.startswith("4"))
            self.assertTrue(luhn.is_valid(n))

    def test_generate_errors(self):
        with self.assertRaises(ValueError):
            luhn.generate("12x")
        with self.assertRaises(ValueError):
            luhn.generate("1234", 4)

    def test_cli(self):
        self.assertEqual(luhn.main(["validar", "79927398713"]), 0)
        self.assertEqual(luhn.main(["validar", "79927398710"]), 1)
        self.assertEqual(luhn.main(["gen", "-p", "1234", "-l", "4"]), 2)


if __name__ == "__main__":
    unittest.main()
