import socket
IP = '10.2.2.243'  # 修改为别人的 IP PORT
port = 29529
address = (IP, port)
cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect(address)
while True:
    msg=input('type your msg')
    msg='C罗：{}'.format(msg)
    cli.send(msg.encode('utf8'))
    remsg= cli.recv(1024)
    print(remsg.decode('utf8'))
    if remsg is None:
        cli.close()
        break


