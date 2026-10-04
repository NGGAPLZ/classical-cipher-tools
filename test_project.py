import unittest
from caesar_decipherer import caesar_shift
from vigenere_cipher import cypher, decypher
from custom_cipher import transform, ALPHABETS

class CipherTests(unittest.TestCase):
    def test_caesar_known_answer(self):
        self.assertEqual(caesar_shift("KHOOR, 123!", 23), "HELLO, 123!")

    def test_vigenere_known_answer(self):
        self.assertEqual(cypher("ATTACK AT DAWN", "LEMON"), "LXFOPV EF RNHR")
        self.assertEqual(decypher("LXFOPV EF RNHR", "LEMON"), "ATTACK AT DAWN")

    def test_invalid_keys(self):
        for key in ("", "123", "A B", "é"):
            with self.subTest(key=key), self.assertRaises(ValueError):
                cypher("HELLO", key)
        for key in ("", "🔑"):
            with self.subTest(key=key), self.assertRaises(ValueError):
                transform("Hello", key)
        with self.assertRaises(ValueError):
            transform("Hello", "key", 5)

    def test_custom_roundtrip_all_orders(self):
        for order, alphabet in ALPHABETS.items():
            text = alphabet + " é🔑\n"
            encoded = transform(text, "Key 123!", order)
            self.assertEqual(transform(encoded, "Key 123!", order, True), text)

    def test_custom_known_answer(self):
        self.assertEqual(transform("abc", "b", 1), "cde")

if __name__ == '__main__':
    unittest.main()
