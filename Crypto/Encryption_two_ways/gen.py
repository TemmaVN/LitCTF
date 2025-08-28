#!/usr/bin/env python3
from Crypto.Util.number import long_to_bytes as ltb, bytes_to_long as btl, getPrime
import os

p = getPrime(1024)
q = getPrime(1024)
flag = btl(b'LITCTF{[redacted]}' + os.urandom(32))
print("Xor cipher:")
print(f'{ltb(flag) = }')
print(f'{ltb(p) = }')
print(f'{ltb(flag ^ p) = }')
print(flag^p)
print(flag^q)

print("RSA:")
e = 65537
N = p*q
print(e,N)
print(pow(flag, e, N))
