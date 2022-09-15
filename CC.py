import string

alphabet = string.ascii_uppercase # "abcdefghijklmnopqrstuvwxyz"

def decrypt():
    encrypted_message = input().strip()
    print(encrypted_message)
    key = int(input())
    
    decrypted_message = ""

    for c in encrypted_message:

        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position + key) % 26
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c

    print(decrypted_message)

decrypt()