"""Repeating-key cipher over four user-selectable ASCII alphabets.

Combines the original Project_Cypher and Project_Decypher algorithms.
This is a learning exercise, not secure encryption or two-factor authentication.
"""
import string

ALPHABETS = {
    1: " " + string.ascii_letters + string.punctuation + string.digits,
    2: string.punctuation + string.ascii_letters + string.digits + " ",
    3: string.digits + string.ascii_letters + " " + string.punctuation,
    4: string.ascii_letters + string.digits + string.punctuation + " ",
}


def transform(text, key, order=1, decrypt=False):
    if order not in ALPHABETS:
        raise ValueError("Alphabet order must be 1, 2, 3, or 4.")
    chars = ALPHABETS[order]
    if not key or any(char not in chars for char in key):
        raise ValueError("Key must be nonempty and contain only printable ASCII characters.")
    key_to_digits = [chars.index(char) for char in key]
    result = ""
    key_index = 0
    direction = -1 if decrypt else 1
    for char in text:
        if char not in chars:
            result += char
        else:
            new_index = (chars.index(char) + direction * key_to_digits[key_index]) % len(chars)
            result += chars[new_index]
            key_index = (key_index + 1) % len(key_to_digits)
    return result


def main():
    print("Custom repeating-key cipher (educational)")
    print("1. Space + Letters + Symbols + Digits")
    print("2. Symbols + Letters + Digits + Space")
    print("3. Digits + Letters + Space + Symbols")
    print("4. Letters + Digits + Symbols + Space")
    try:
        order = int(input("Alphabet order (1-4): "))
        mode = input("Encrypt or decrypt (e/d): ").strip().lower()
        if mode not in ("e", "d"):
            raise ValueError("Mode must be e or d.")
        text = input("Text: ")
        key = input("Key: ")
        print(transform(text, key, order, decrypt=mode == "d"))
    except ValueError as error:
        print(f"Input error: {error}")


if __name__ == "__main__":
    main()
