Vigenere-Cipher

Description:
This Python program implements the Vigenère Cipher, a classic encryption technique, for teaching and code analysis purposes. It enables users to encrypt and decrypt messages using a provided key. The code emphasizes modularity and user-friendly input handling. The code also utilizes a wide variety of logic, statements, and built-in functions, making it ideal for teaching intermediate Python principles. Below is a step-by-step map of the code logic:

Step 1: Import Modules and Constants

The code starts by importing the string module, which provides the constant string.ascii_lowercase, representing all lowercase letters of the English alphabet.

Step 2: Build a Key Matching Text Length

The build_key function is introduced to generate a key that matches the length of the input text while accounting for spaces and special characters. It evenly repeats characters from the encryption key to match the text's length.

Step 3: Vigenère Cipher Algorithm

The core of the Vigenère Cipher algorithm is implemented in the vigenere_cipher function. This function handles both encryption and decryption, depending on the decrypt flag.

Encryption: It iterates through each character of the input text. For each alphabetic character, it calculates a shift value based on the corresponding character in the encryption key and applies the shift to produce the encrypted character. Uppercase letters are maintained as uppercase in the result.

Decryption: Similar to encryption, but with a reverse shift to decrypt the message. It also maintains the case of the original text.

Step 4: User's Choice (Encrypt or Decrypt)

The program prompts the user to choose between encryption and decryption by entering 'e' or 'd'.

Step 5: Input Text

The user is asked to input the text they want to encrypt or decrypt. The program validates that the input contains at least one alphanumeric character.

Step 6: Input Encryption Key

The user provides an encryption key. The program validates that the key contains at least one character and only consists of alphabetic characters.

Step 7: Execute the Chosen Operation

The appropriate function (encryption or decryption) is called with the provided text and key. The result is displayed to the user.
