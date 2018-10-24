# 1.读取图片
# 2. 传递读取之后的信息
import os
import socket

pics = b''
base_file = os.path.abspath(__file__)
file_dir = os.path.dirname(base_file)
pic_file_path = os.path.join(file_dir,'cluo.jpg')
# a = os.path.join(os.path.dirname(os.path.abspath(__file__)),'cluo.jpg')
ip = '127.0.0.1'
port=33333
addr = (ip,port)

ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.connect(addr)

with open (pic_file_path,'rb+') as f:  # open是puthon 交给系统底层打开的，不是python打开的
    while 1:
        data = f. read(1024)
        if not data:
            break
        pics += data

ss.send(pics)
ss.close()
# pic_file_copy_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'cluo2.jpg')
# with open(pic_file_copy_path,'wb+') as f:
#     f.write(pics)
