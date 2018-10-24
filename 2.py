import socket
"""client"""
addr=('0.0.0.0',19562)
ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.connect(addr)
while 1:
    info = input('--->')
    ss.send(info.encode('utf8'))
    msg=ss.recv(1024)
    msgs = msg.decode('utf8')
    print(msgs)
    if msgs =='86':
        ss.close()