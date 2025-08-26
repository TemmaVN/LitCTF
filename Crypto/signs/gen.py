#!/usr/bin/env python3
from Crypto.Util.number import getPrime, bytes_to_long as btl,long_to_bytes as ltb
from Crypto.Util.Padding import pad as hashing

with open('flag','r') as f:
	flag = f.readline().rstrip()

p = getPrime(1024)
q = getPrime(1024)
n = p*q
e = 65537
t = (p-1)*(q-1)
d = pow(e, -1, t)

print(f"{e = }")
print(f"{n = }")

flag = flag.encode()
enc = pow(btl(flag), e, n)
print(f"{enc = }")

sign = pow(btl(hashing(flag, 256)), d, n)
print(f"{sign = }")

print(f'{ltb(pow(sign,e,n)) = }')
'''
e
n
c = pow(flag,e,n)
hash = (flag * 256**(count + 1) + (256 ** (count +1) - 1) // 255)**d

'''

