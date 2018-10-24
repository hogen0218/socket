import socket
pics = b''
addr=("0.0.0.0",19562)
#tcp协议
ss = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ss.connect(addr)
#python 调用系统底层
while True:
    data = input('data:')
    ss.send(data.encode('utf8'))
    data = ss.recv(1024)
    print(data)