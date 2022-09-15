import requests
import json
import string
import re
import time
for t in range(1000):
    # time.sleep(1.5)
    headers = {"Authorization": "Bearer 65e97410dd246b41ab39e122f91f00c0ae46d4a7018b0c887ccf500b8707cf7fd1bbe1c574d313d8727a25dfa2bacdebee67a66aee295f20fe67bf3895e10fa3d4438d3508a086d27fcb001e3de68dc15646ae79d9a18c812532dc5da699ba3da19123d7c104c56cdb94ecf53f87f002002c6b9e53377834c0ee5f78206978e7141ad21d05fd27361968edb880ea1271dd68b91886c9a9bbf6cd6a4eb912ae639d9e69e2c1caa5fe8edd8baf31d4611892fa644e64190b25511bc4a49f830fd20a01949784ecd735da8b33e1bac1a30c90c484dfd3abe6c6bb13b82e5b82b5409e0a98d5a00a92afdf8a12a45c8ed4ab4fb5838c43f92b6c4ba6c71faafba79e", "Content-type":"application/json"}
    x = requests.get('https://cracking-the-code-api.herokuapp.com/caesar/decrypt', headers=headers)
    m = x.text

    a=re.split('"key":|"cipher":|"|,', m)


    y = a[1]
    z = a[4]


    # a=m.get('key')
    # print(a)



    alphabet = string.ascii_uppercase # "abcdefghijklmnopqrstuvwxyz"

    def decrypt():
        
        encrypted_message = z.strip()
    
        key = int(y)
        
        decrypted_message = ""

        for c in encrypted_message:

            if c in alphabet:
                position = alphabet.find(c)
                new_position = (position - key) % 26
                new_character = alphabet[new_position]
                decrypted_message += new_character
            else:
                decrypted_message += c
        myobj = {'message': decrypted_message}
        q = requests.post('https://cracking-the-code-api.herokuapp.com/caesar/decrypt', headers=headers, json=myobj)
        print(q.text)
    decrypt()