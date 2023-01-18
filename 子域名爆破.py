import socket
import time
for  Subdomain in open('D:\safetools\dic.txt'):
    Su = Subdomain.replace('\n','')
    url = Su + '.'+'xueersi.com'
    try:
        ip=socket.gethostbyname(url)
        print(url+'->'+ip)
        time.sleep(0.01)
    except Exception as e:
        pass   