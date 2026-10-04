# Classical Cipher Tools

Three small Python exercises exploring modular arithmetic and repeating keys.

- `caesar_decipherer.py`: prints all 25 nonzero shifts of an uppercase message.
- `vigenere_cipher.py`: encrypts and decrypts using a letter-only key.
- `custom_cipher.py`: the original custom cipher, with four selectable orders of printable ASCII characters. Encryption and decryption are now in one script.

## Run

Use Python 3.12 or newer. No third-party packages are required.

```sh
python caesar_decipherer.py
python vigenere_cipher.py
python custom_cipher.py
```

For Caesar, enter `KHOOR`; shift 23 produces `HELLO`.
For Vigenere, choose `1`, enter `ATTACK AT DAWN` and key `LEMON`;
the result is `LXFOPV EF RNHR`. Choose `2` with the same key to reverse it.
The Vigenere command-line tool uppercases input; its Python functions expect uppercase text and keys.

The custom cipher requires the same key and alphabet order to decode a message.
Unsupported message characters pass through unchanged and do not advance the key.
Keys must be nonempty and use supported characters.

These are classical cipher demonstrations, not secure encryption. The custom
alphabet option is not two-factor authentication. Do not use these tools to protect secrets.

## Test

```sh
python -m unittest -v
```

## Project history

See [CHANGES.md](CHANGES.md) for the preparation notes.

No distribution license has been selected for this project.
