#!/usr/bin/env python3

from pwn import *
from Crypto.Util.number import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad 

p = 15471456606036645889
x1 = 3681934504574973317
x2 = 4155039551524372589
x3 = 9036939555423197298
iv = long_to_bytes(0x6c9315b13f092fbc49adffbf1c770b54)
c = long_to_bytes(0xaf9dc7dfd04bdf4b61a1cf5ec6f9537819592e44b4a20c87455d01f67d738c035837915903330b67168ca91147299c422616390dae7be68212e37801b76a74d4)

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

'''
lcg.a = 17724163341775641095 lcg.b = 11134563501582661490 lcg.x = 9005999471342510619
17515121380922568731
3708297254059389350
11314559209260025601
12559035663876982285
r = 3925915838665343029
eeb63b042151748fa1964a38a17f4dff
1700f49d5a16c3f27fd513dbe938e223ac0ff0c6674e68ab6d1abaff1d167827


'''

for i in range(101):
	x1,x2,x3 = Back_track(x1,x2,x3)

log.info(f'{x1 = } {x2 = } {x3 = }')

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

lcg = LCG(x1,x2,x3)
r = lcg.next()
log.info(f'{r = }')
key = pad(long_to_bytes(r**2),16)
cipher = AES.new(key,AES.MODE_CBC,iv = iv)
flag = cipher.decrypt(c)
log.info(f'{flag = }')