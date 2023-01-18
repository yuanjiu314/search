import socket
import os,sys
import time
import whois
def Cnd(url):
    cdn_data =os.popen('nslookup %s'%url).read()#读取对象返回字符串
    num = cdn_data.count('.')
    print(cdn_data)
def webwhois(url):
    print(whois.whois(url))
   
def Subdomain(url):###子域名爆破模块
    urls = url.replace('www','')
    for  Subdomain in open('D:\safetools\dic.txt'):
        Su = Subdomain.replace('\n','')
        url = Su + str(urls)
        print(url)
        try:
            ip=socket.gethostbyname(url)
            print(url+'->'+ip)
            time.sleep(0.01)
        except Exception as e:
            pass 
def Domian_ip(url):
    ip = socket.gethostbyname(url)
    print(ip)
    return ip
def Ip_Port(url):
    IP = socket.gethostbyname(url)
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #建立对象
    ports = {'21','22','135','443','445','80','1433','3306',"3389",'1521','8000','7002','7001','8080',"9090",'8089',
    '4848'}#端口扫描：1.1-65535 2.常见端口
    for port in ports:
        result=server.connect_ex((IP,int(port)))#()元组，[]列表，{}字典
        print(result)
        if result == 0:
            print(port+'||open')
        else:
            print(port+'||close')
if __name__ == '__main__':
    #p0 = sys.argb[0] #0指代码（即此.py程序）本身的意思
    p1 = sys.argv[1] #1指第一个输入
    url = sys.argv[2]
    #try: 
    if p1 == '-cnd':
         Cnd(url)
    if p1 == '-ip':
        Domian_ip(url)
    if p1 == '-whois':
        webwhois(url)
    if p1 == '-port':
        Ip_Port(url)
    if p1 == '-sub':
        Subdomain(url)
    if p1 == '-all':
        Cnd(url)
        Domian_ip(url)
        webwhois(url)
        Ip_Port(url)   
        Subdomain(url)    
    #except Exception as a:
        #print('error:wrong parameter')    
    

    
        
        
        