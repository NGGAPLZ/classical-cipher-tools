"""
Caesar Cipher Decipherer

This program takes a Caesar-cipher encrypted message and prints all
25 possible shifts. Since a Caesar cipher only has 25 useful keys,
brute-forcing every possible shift is simple.
"""

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def caesar_shift(text, shift):
    """
    Shift each letter in the text by the given amount.

    Non-letter characters such as spaces, numbers, and punctuation
    are preserved.
    """
    decrypted_text = ""

    for character in text:
        if character not in ALPHABET:
            decrypted_text += character
        else:
            old_index = ALPHABET.index(character)
            new_index = (old_index + shift) % 26
            decrypted_text += ALPHABET[new_index]

    return decrypted_text


def main():
    print("Caesar Cipher Decipherer")
    print("This program prints all 25 possible Caesar cipher shifts.")
    print()

    encrypted_message = input("Paste the encrypted message here: ").upper()

    print()
    print("Possible decryptions:")
    print("-" * 40)

    for shift in range(1, 26):
        possible_message = caesar_shift(encrypted_message, shift)
        print(f"Shift {shift:2}: {possible_message}")


if __name__ == "__main__":
    main()