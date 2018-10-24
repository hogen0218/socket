import socket
"""server"""
addrs=("0.0.0.0",19562)
ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.bind(addrs)
ss.listen()

while 1:
    cli,addr =ss.accept()
    print('from {} msg:'.format(addr))
    while 1:

        msg = cli.recv(1024)
        msgs=msg.decode('utf8')
        print(msg)
        info = input('--->')
        cli.send(info.encode("utf8"))
        if msgs=='88':
            cli.send(b'86')
            ss.close()

