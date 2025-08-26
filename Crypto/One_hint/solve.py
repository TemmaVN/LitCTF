#!/usr/bin/env python3
from pwn import *
from Crypto.Util.number import *

cipher_text = 'fkxlafg_plk_qkuxbkgp_hucknkxk_khkx'
plain_text = 'redacted'

OFFSET = 26
NUM_PART = 2345	


res_test = ''
for i in plain_text:
	tg = ord(i) - ord('a')
	res_test += chr((tg*pow(3,2345,26))%26 + ord('a'))

log.info(f'{res_test = }')

Flag = ''
def solve(c):
	res = ''
	num_tg = inverse(3**2345,26)
	for i in c:
		if i == '_':
			res += i 
			continue
		tg = ord(i) - ord('a')
		res += chr((tg*num_tg)%26 + ord('a'))
	return res 

log.info(f'{solve(cipher_text) = }')