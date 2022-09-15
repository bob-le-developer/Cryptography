import hashlib

num = int(input('Block number: '))
tag = int(input())
path = '/Users/zhangwanwan/Downloads/W2U3/__pycache__/blocks/block{}.dat'.format(num)
data = open(path, "r")
block = "".join(data.readlines()).strip()

blockdata = block + str(tag)

cipher= hashlib.md5(blockdata.encode()).hexdigest()
print(cipher)