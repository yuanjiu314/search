import os
import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立对象
ports = {'21','22','135','443','445','80','1433','3306',"3389",'1521','8000','7002','7001','8080',"9090",'8089',
'4848'}#端口扫描：1.1-65535 2.常见端口
for port in ports:

    result=server.connect_ex(('47.75.212.155',int(port)))#()元组，[]列表，{}字典
    
    if result == 0:
        print(port+'||open')
    else:
        print(port+'||close')