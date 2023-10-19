import string

# Define the English alphabet in lowercase
LETTERS = string.ascii_lowercase

# Function to let the user choose an encryption/decryption key
def choose_key():
    while True:
        key = input('Enter the encryption/decryption key (number 1-25): ')
        if key in [str(x) for x in range(1, 26)]:
            return int(key)
        print('\nPick a valid key')

# Function to perform Caesar cipher encryption or decryption
def encrypt(text, key, decrypt=False):
    new = []
    for i, c in enumerate(text.lower()):
        if not c in LETTERS:
            new.append(c)
        else:
            shift = key if not decrypt else -key
            new_char = LETTERS[(LETTERS.index(c) + shift) % 26]
            new.append(new_char.upper() if text[i].isupper() else new_char)
            
    return "".join(new)

# Function to let the user choose the encryption/decryption method
def choose_method():
    while True:
        method = input('\nDo you want to encrypt or decrypt the text? (\'e\' or \'d\')').lower()
        if method.startswith('e') or method.startswith('d'):
            return method.startswith('d')
            
        print('\nEnter a valid answer')

# Function to get the text input from the user
def create_text():
    while True:
        text = input('\nEnter the text: ')
        if any(x.isalpha() for x in text):
            return text
        print('\nEnter a valid text with at least one letter')

# Function to let the user decide whether to brute force the key
def crack():
    while True:
        answer = input('\nWould you like to Brute Force the Key? (\'y\' or \'n\'): ').lower()
        if answer.startswith('y') or answer.startswith('n'):
            return answer.startswith('y')
        print('\nCome again?')

# Function to brute force the Caesar cipher key
def brute_force(text):
    for i in range(1, len(LETTERS)):
        print(f'{i}: {encrypt(text, i, decrypt=True)}')

# Function to let the user try to solve the Caesar cipher key
def solve(key):
    return input('What is the key?: ') == str(key)

# Function to ask the user if they want to repeat the process
def replay():
    while True:
        re = input('Go again? (\'y\' or \'n\'): ')
        if re.startswith('y') or re.startswith('n'):
            return re.startswith('y')
        print('Invalid input')

# Main function to run the Caesar cipher program
def main():
    print('''Welcome to Caesar's Cryptography Castle!
    
    This program is designed to teach encryption concepts as well as Python code.
    Here is a brief walkthrough of how Caesar Cipher encryption works and how it is implemented in this code:
    
    1. The user must first input a text string
    2. The user must then input a numeric key between 1-25
    4. The user will specify whether to use the encryption or decryption algorithm
    5. The program will then shift each letter of the text according to the user's choice of key (x steps forward for encryption and x steps back for decryption)
    6. This program returns the ciphertext or plain text to the user
    
    I hope this made sense. Enjoy!\n''')

    while True:
        key = choose_key()
        text = create_text()
        method = choose_method()
        code = encrypt(text, key, decrypt=method)
        print(code)

        if not method:
            if crack():
                print('\nLet\'s crack this code...')
                brute_force(code)
                guess = solve(key)
                if guess:
                    print('Correct!')
                else:
                    print('Wrong!')

        re = replay()

        if not re:
            break

if __name__ == "__main__":
    main()  # Run the main program
