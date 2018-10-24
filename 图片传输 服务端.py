import os
import socket

ip = '127.0.0.1'
port=33333
addr = (ip,port)
pics = b''
ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.bind(addr)
ss.listen(2)
conn,addr = ss.accept()
while 1:
    data = conn.recv(1024)
    if not data:
        break

    pics += data




pic_file_copy_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'cluo2.jpg')
with open(pic_file_copy_path,'wb+') as f:
    f.write(pics)