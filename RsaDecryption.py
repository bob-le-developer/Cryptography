import rsa
import requests
import string
import re

headers = {"Authorization": "Bearer 6ec02eddf12e53f500acad1c464baf1f575f0eba7f28644e7e96b81550284fe7da179ba3acf9f539f3d8aa8b034c5d51dfb3bb716bf74da9b64ba352155745adbe7a55f23d0d865439ec530fa6faaa042bd105a64328ef71dab4debf2386c91bbb0317f4ac6d092c59920ecfa507df04791dc45f228dbc03fba5ece5e49ce9fdf649dbd74c92d8c4ad61d022119409aec1aa9d47490e4a283c3bdec46ff8d9a5adc48c60625b66e04bded812980f2be30de9bbbb2a2ac67610dccd27e1aae95f6d68b9ab04cbfe3fd8125f76cb211accbd30f21b5e81e8fe30f6f86e3ded85bdf8d05b23791e220d663cfda3551627dd3091b6c3f13d9a5203d03e0396ee2ba1", "Content-type":"application/json"}
x = requests.get('https://cracking-the-code-api.herokuapp.com/caesar/encrypt', headers=headers)
m = x.text

a=re.split('"n":|"message":|"|,', m)

y = a[1]
z = a[4]

n = int(input())
e = int(input())
message = int(input())
MexpN = pow(message, e)
answer = MexpN % n
print(answer)

myobj = {'cipher': answer}
q = requests.post('https://cracking-the-code-api.herokuapp.com/caesar/encrypt', headers=headers, json=myobj)
print(q.text)