import hashlib

num = int(input('Block number: '))
path = '/Users/zhangwanwan/Downloads/W2U3/__pycache__/blocks/block{}.dat'.format(num)
data = open(path, "r")
block = "".join(data.readlines()).strip()

y = False

z = 2000000
cipher = ""

while cipher[:6] !="000000":
    cipher=(hashlib.md5((block+str(z)).encode())).hexdigest()
    z+=1
print(z)
print(cipher)

