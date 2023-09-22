import string

ALPHABET = string.ascii_lowercase

def build_key(text, key):
    '''
    Stretch a key to match the length of the text
    '''

    # Starting blank key and beginning index
    new_key = ''
    key_index = 0

    # extend key to match length of text, accounting for spaces and puncuation
    for char in text:
        if char.isalpha():
            new_key += key[key_index].lower()
            key_index = (key_index + 1) % len(key)
        else:
            new_key += char

    return new_key

def vigenere_cipher(text, key, decrypt=False):
    '''
    Encrypt or decrypt (depending on the decrypt flag) text against key.
    '''
    # parameters - empty new text, extended key, and value of 26
    result = []
    key = build_key(text, key)
    alphabet_len = 26

    # Calculates and applies letter shift
    for i, char in enumerate(text):
        if char.isalpha():
            shift = ALPHABET.index(key[i]) if not decrypt else -ALPHABET.index(key[i])
            new_char = ALPHABET[(ALPHABET.index(char.lower()) + shift) % alphabet_len]

            # Matches uppercase letters in new text
            if char.isupper():
                new_char = new_char.upper()

            result.append(new_char)
        # Append spaces or puncuation unchanged
        else:
            result.append(char)

    return ''.join(result)
    
def main():
    # User's Choice (Encrypt or Decrypt)
    while True:
        operation = input("Hello, user. Will you be encrypting or decrypting a message? (enter 'e' or 'd'): ").lower()

        if operation.startswith('e'):
            decrypt = False
        elif operation.startswith('d'):
            decrypt = True
        else:
            print("\nPlease enter 'e' for encryption or 'd' for decryption.\n")
            continue

        # Step 5: Input Text
        while True:
            text = input("Enter the text: ")
            if not any([x.isalpha() for x in text]):
                print('Enter a text with at least 1 alphanumeric character.\n')
            else:
                break

        # Step 6: Input Encryption Key
        while True:
            key = input("\nEnter an encryption key: ")
            if not key:
                print("\nPlease enter a key of at least 1 character (longer key recommended).\n")
            elif not key.isalpha():
                print("\nYour key cannot contain numbers or special characters.\n")
            else:
                break

        # Step 7: Execute the Chosen Operation
        result = vigenere_cipher(text, key, decrypt)
        print('\nResult:', result, '\n')

if __name__ == "__main__":
    main()
