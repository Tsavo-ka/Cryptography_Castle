import string

ALPHABET = string.ascii_lowercase

def build_key(text, key):
    new_key = ''
    key_index = 0

    for char in text:
        if char.isalpha():
            new_key += key[key_index].lower()
            key_index = (key_index + 1) % len(key)
        else:
            new_key += char

    return new_key

def vigenere_cipher(text, key, decrypt=False):
    result = []
    key = build_key(text, key)
    alphabet_len = len(ALPHABET)

    for i, char in enumerate(text):
        if char.isalpha():
            shift = ALPHABET.index(key[i]) if not decrypt else -ALPHABET.index(key[i])
            new_char = ALPHABET[(ALPHABET.index(char.lower()) + shift) % alphabet_len]

            if char.isupper():
                new_char = new_char.upper()

            result.append(new_char)
        else:
            result.append(char)

    return ''.join(result)

def main():
    while True:
        operation = input("Hello, user. Will you be encrypting or decrypting a message? (enter 'e' or 'd'): ").lower()

        if operation.startswith('e'):
            decrypt = False
        elif operation.startswith('d'):
            decrypt = True
        else:
            print("\nPlease enter 'e' for encryption or 'd' for decryption.\n")
            continue

        text = input("Enter the text: ")
        if not text:
            print('Enter a text of at least 1 alphanumeric character.\n')
            continue

        key = input("\nEnter an encryption key: ")
        if not key:
            print("\nPlease enter a key of at least 1 character (longer key recommended).\n")
            continue
        elif not key.isalpha():
            print("\nYour key cannot contain numbers or special characters.\n")
            continue

        result = vigenere_cipher(text, key, decrypt)
        print('\nResult:', result, '\n')

if __name__ == "__main__":
    main()
