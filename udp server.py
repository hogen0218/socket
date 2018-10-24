import socket
addr=("0.0.0.0",19562)
ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.bind(addr)


while 1:
    data,addr= ss.recvfrom(1024)
    ss.sendto(data, addr)
