"""Classical Vigenere cipher; educational, not secure encryption."""
import string

alphabet = string.ascii_uppercase


def repeat_key(user_text, user_key):
    """
    Repeats the user key to match the length of the user text.

    :param user_text: The text to be processed.
    :param user_key: The encryption/decryption key.
    :return: A repeated version of the key that matches the length of the text.
    """
    if not user_key or any(char not in alphabet for char in user_key):
        raise ValueError("Key must contain only letters A-Z and cannot be empty.")
    repeated = ""
    key_index = 0

    for char in user_text:
        if char in alphabet:
            repeated += user_key[key_index]
            key_index += 1
            if key_index == len(user_key):
                key_index = 0
        else:
            repeated += char
    return repeated


def cypher(user_text, key):
    """
    Encrypts the text using the Vigenère Cipher.

    :param user_text: The plain text to be encrypted.
    :param key: The encryption key.
    :return: The encrypted message.
    """
    result = ""
    repeated_key = repeat_key(user_text, key)

    for i in range(len(user_text)):
        text_char = user_text[i]
        key_char = repeated_key[i]

        if text_char in alphabet:
            text_pos = alphabet.index(text_char)
            key_pos = alphabet.index(key_char)

            new_pos = (text_pos + key_pos) % 26
            result += alphabet[new_pos]
        else:
            result += text_char

    return result


def decypher(user_text, key):
    """
    Decrypts the text using the Vigenère Cipher.

    :param user_text: The encrypted message to be decrypted.
    :param key: The decryption key.
    :return: The decrypted plain text.
    """
    result = ""
    repeated_key = repeat_key(user_text, key)

    for i in range(len(user_text)):
        text_char = user_text[i]
        key_char = repeated_key[i]

        if text_char in alphabet:
            text_pos = alphabet.index(text_char)
            key_pos = alphabet.index(key_char)

            new_pos = (text_pos - key_pos) % 26
            result += alphabet[new_pos]
        else:
            result += text_char

    return result



def main():
    print("Vigenere Cipher (educational)")
    main_choice = input("Enter 1 for Cipher, or 2 for Decipher: ").strip()
    while main_choice not in ("1", "2"):
        main_choice = input("Enter 1 or 2: ").strip()
    user_text = input("Enter the text: ").upper()
    user_key = input("Enter the key (letters A-Z): ").upper()
    try:
        print(cypher(user_text, user_key) if main_choice == "1" else decypher(user_text, user_key))
    except ValueError as error:
        print(f"Input error: {error}")


if __name__ == "__main__":
    main()
