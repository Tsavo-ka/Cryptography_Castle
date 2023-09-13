import string
letters = [x for x in string.ascii_lowercase]

my_keys = {}
counter = 0
for l in letters:
    my_keys[l] = counter
    counter += 1

def key_build(text, key):
    '''
    This function will stretch or compress the user's key to match the length of the text, accounting for special characters
    '''
    new = ""
    ind = 0
    
    while len(new) < len(text):
        
        for c in text:
            
            if not c.isalpha():
                new += c
            else:
                new += key[ind].lower()
                if ind == len(key)-1:
                    ind = 0
                else:
                    ind += 1
            
    return new

def encrypt(text, key):
    '''
    This function takes in the user's text and ENCRYPTS it against the user's key, returning cypher text
    '''
    cypher = []
    l_text = text.lower()
    
    key = key_build(text, key)
    

    for i, c in enumerate(l_text):
        if not c.isalpha():
            cypher += c
        elif ord(c) + my_keys[key[i]] > 122:
            cypher += chr(abs(ord(c) + my_keys[key[i]] - 123) + 97)
        else:
            cypher += chr(ord(c) + my_keys[key[i]])
        
    for i, c in enumerate(text):
        if c.isupper():
            cypher[i] = cypher[i].upper()
    
    return "".join(cypher)

def decrypt(text, key):
    '''
    This function takes in the user's text and DECRYPTS it against the user's key, returning plain text
    '''
    plain = []
    l_text = text.lower()
    
    key = key_build(text, key)
    

    for i, c in enumerate(l_text):
        if not c.isalpha():
            plain += c
        elif ord(c) - my_keys[key[i]] < 97:
            plain += chr(abs(abs(my_keys[c] - my_keys[key[i]]) - 123))
        else:
            plain += chr(ord(c) - my_keys[key[i]])
        
    for i, c in enumerate(text):
        if c.isupper():
            plain[i] = plain[i].upper()
    
    return "".join(plain)

print(""",   .     .                     .         ,  ,       .   .   p     
| . |     |                     |         | /      o |   |         
| ) ) ,-. | ,-. ,-. ;-.-. ,-.   |-  ,-.   |<   ,-. . |-  |-.   ,-. 
|/|/  |-' | |   | | | | | |-'   |   | |   | \\  |-' | |   | |   `-. 
' '   `-' ' `-' `-' ' ' ' `-'   `-' `-'   '  ` `-' ' `-' ' '   `-' 
                                                                   """)

print("""██╗   ██╗██╗ ██████╗ ███████╗███╗   ██╗███████╗██████╗ ███████╗     ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗ 
██║   ██║██║██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔════╝    ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗
██║   ██║██║██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝█████╗      ██║     ██║██████╔╝███████║█████╗  ██████╔╝
╚██╗ ██╔╝██║██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══╝      ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
 ╚████╔╝ ██║╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║███████╗    ╚██████╗██║██║     ██║  ██║███████╗██║  ██║
  ╚═══╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚══════╝     ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                              """)
print(""" ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                             """)


run = True

while run:

    #Choose encryption or decryption function
    while True:
        operation = input("Hello, user. Will you be encrypting or decrypting a message? (enter 'e' or 'd'): ").lower()
        if operation.startswith('e') or operation.startswith('d'):
            break
        else:
            print("\nplease enter a valid answer\n")

    # Take a text to encrypt/decrypt
    while True:
        text = input("Enter the text: ")
        if text:
            break
        print('Enter a text of at least 1 alphanumeric character')
    

    # Take a key for encryption/decryption
    while not key or not key.isalpha():
        key = input("\nPlease enter an encryption key: ")
        if not key:
            print("\nPlease enter a key of at least 1 character (longer key recommended")
        elif not key.isalpha():
            print("\nYour key cannot contain numbers or special characters")

    # Run encryption/decryption depending on user's initial choice
    if operation.startswith('e'):
        new_text = encrypt(text, key)
    else:
        new_text = decrypt(text, key)

    
    if operation.startswith('e'):
        print(f"\nYour encrypted text:\n\n\t{new_text}\n")
    else:
        print(f"\nYour decrypted text:\n\n\t{new_text}\n")
