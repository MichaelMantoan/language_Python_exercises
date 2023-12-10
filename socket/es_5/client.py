import sys,socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
s.connect((sys.argv[1],int(sys.argv[2])))
file = open(sys.argv[3],"r")
text = file.read()
s.send(text.encode())
data= s.recv(1024).decode()
file2 = open(sys.argv[4],"w")
file2.write(data)
s.close()