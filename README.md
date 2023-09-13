# Vigenere-Cipher
A Python Vigenere Cipher Generator for teaching/analysis purposes. 

This code was written using only basic python coding logic and one simple module and is meant as a tool for teaching python coding logic

Comments, suggestions, and critiques are very much appreciated

Here is a run-through of the code's logic:

Step 1:

Import the strings module and build a list of all lowercase letters

Step 2:

Run through the list and assign each letter as a dictionary key with a corresponding number value, starting at 0 and incrementing by 1 each letter
the printed dictionary would look like this:

{'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17,
's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

Step 3:

Make a function that either stretches (duplicates characters) or compresses (deletes characters) from the key to make it match the length of the text,
accounting for spaces and special characters

Step 4:

Make a function for the Encryption process:

Use a for loop to iterate through every character of the text and add its ASCII (ord()) value to the number value (contained in the dictionary above of 
the corresponding character of the encryption key. 

If the ASCII value + the key value is higher than 122 (the value of 'z'), then we find the absolute value
of (character ASCII value + key value - 123) + 97 and return the letter value of the outcome (using chr())

Else, we simply add the character number value to the key number value.

Step 5:

Make a function for the Decryption process:

Ths function works exactly like the encryption one, just with a slightly different math algorithm

Step 6:

Let the user decide with an input whether they wish to use the encryption or the decryption algorithm

Step 7:

Take a text for enc/dec from the user

Step 8:

Take an enc/dec key from the user

Step 9:

Run the appropriate function

fin
