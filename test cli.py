import socket
IP = '10.2.4.64'  # 修改为别人的 IP PORT
port = 8812
address = (IP, port)
cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect(address)
while True:
    msg=input('type your msg')
    msg = '马塞洛：{}'.format(msg)
    cli.send(msg.encode('utf8'))
    remsg= cli.recv(1024)
    print(remsg.decode('utf8'))
    if remsg is None:
        cli.close()
        break
