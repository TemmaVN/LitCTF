#!/usr/bin/env python3
# inferior rngs
from random import SystemRandom
random = SystemRandom()
from Crypto.Util.number import getPrime, inverse
p = getPrime(64)
def Back_track(x1,x2,x3):
    '''
    a*x + b = x1
    a*x1 + b = x2
    a*x2 + b = x3
    '''
    x2_x1 = inverse((x2-x1),p)
    a = pow((x3-x2)*x2_x1,1,p)
    b = (x3 - a*x2)%p 
    a_1 = inverse(a,p)
    x = pow((x1-b)*a_1,1,p)
    return a,b,x 

class LCG:
    def __init__(self, a, b, x):
        self.a = a
        self.b = b
        self.x = x
        self.m = p
    def next(self):
        self.x = (self.a * self.x + self.b) % self.m
        ret = self.x
        return ret

class LCG2:
    def __init__(self, baselcg, n=100):
        self.lcg = baselcg
        for i in range(n):
            a = self.lcg.next()
            b = self.lcg.next()
            x = self.lcg.next()
            self.lcg = LCG(a,b,x)
    def next(self):
        return self.lcg.next()

a = random.randint(1, 2**64)
b = random.randint(1, 2**64)
x = random.randint(1, 2**64)
lcg = LCG(a, b, x)
print(f'{lcg.a = } {lcg.b = } {lcg.x = }')
lcg2 = LCG2(lcg)
print(f'{lcg.a = } {lcg.b = } {lcg.x = }')
print(p)
for x in range(3):
    print(lcg2.next())
print(f'{lcg.a = } {lcg.b = } {lcg.x = }')
from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes as l2b
from Crypto.Util.Padding import pad
from os import urandom
r = lcg.next()
print(f'{r = }')
k = pad(l2b(r**2), 16)
iv = urandom(16)
cipher = AES.new(k, AES.MODE_CBC, iv=iv)
print(iv.hex())
f = open("flag.txt",'rb').read().strip()
enc = cipher.encrypt(pad(f,16))
print(enc.hex())
