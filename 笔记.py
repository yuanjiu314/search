import socket
import os,sys
from test import test
import time


###获取目标
###判断CDN信息（cmd:nslookup+域名）



#域名反查IP功能
'''
ip=socket.gethostbyname('www.baidu.com')
print(ip)
'''


#识别目标是否存在CDN
#采用nslookup执行结果进行返回IP解析数目判断
#利用python去调用执行系统命令
#cdn_data =os.system('nslookup www.baiduc.com')#回显不满足需求
#cdn_data =os.popen('nslookup www.baiduc.com')#回显对象
'''
cdn_data =os.popen('nslookup www.xiaodi8.com').read()#读取对象返回字符串
num = cdn_data.count('.')
print(cdn_data)
'''
#端口扫描
#1.原生态：自写socket协议TCP，UDP扫描
#2.调用第三方库massscan，nmap模块等扫描
#3.调用系统工具脚本执行

##原生态：端口批量扫描工具
'''
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立对象
ports = {'21','22','135','443','445','80','1433','3306',"3389",'1521','8000','7002','7001','8080',"9090",'8089',
'4848'}
for port in ports:

    result=server.connect_ex(('47.75.212.155',int(port)))#()元组，[]列表，{}字典
    #端口扫描：1.1-65535 2.常见端口
    if result == 0:
        print(port+'||open')
    else:
        print(port+'||close')
'''

'''
常见端口：{'21','22','135','443','445','80','1433','3306',"3389",'1521','8000','7002','7001','8080',"9090",'8089',
'4848'}
1,web类(web漏洞/敏感目录)


第三方通用组件漏洞struts thinkphp jboss ganglia zabbix

80 web 
80-89 web 
8000-9090 web
2,数据库类(扫描弱口令)

1433 MSSQL 
1521 Oracle 
3306 MySQL 
5432 PostgreSQL 
3,特殊服务类(未授权/命令执行类/漏洞)

443 SSL心脏滴血 
873 Rsync未授权 
5984 CouchDB http://xxx:5984/_utils/ 
6379 redis未授权 
7001,7002 WebLogic默认弱口令，反序列 
9200,9300 elasticsearch 参考WooYun: 多玩某服务器ElasticSearch命令执行漏洞 
11211 memcache未授权访问 
27017,27018 Mongodb未授权访问 
50000 SAP命令执行 
50070,50030 hadoop默认端口未授权访问
4,常用端口类(扫描弱口令/端口爆破)

21 ftp 
22 SSH 
23 Telnet 
2601,2604 zebra路由，默认密码zebra
3389 远程桌面
端口合计详情

21 ftp 
 
22 SSH 
 
23 Telnet 
 
80 web 
 
80-89 web 
 
161 SNMP 
 
389 LDAP 
 
443 SSL心脏滴血以及一些web漏洞测试 
 
445 SMB 
 
512,513,514 Rexec 
 
873 Rsync未授权 
 
1025,111 NFS 
 
1433 MSSQL 
 
1521 Oracle:(iSqlPlus Port:5560,7778) 
 
2082/2083 cpanel主机管理系统登陆 （国外用较多）
 
2222 DA虚拟主机管理系统登陆 （国外用较多） 
 
2601,2604 zebra路由，默认密码zebra
 
3128 squid代理默认端口，如果没设置口令很可能就直接漫游内网了 
 
3306 MySQL 
 
3312/3311 kangle主机管理系统登陆 
 
3389 远程桌面 
 
4440 rundeck 参考WooYun: 借用新浪某服务成功漫游新浪内网 
 
5432 PostgreSQL 
 
5900 vnc 
 
5984 CouchDB http://xxx:5984/_utils/ 
 
6082 varnish 参考WooYun: Varnish HTTP accelerator CLI 未授权访问易导致网站被直接篡改或者作为代理进入内网 
 
6379 redis未授权 
 
7001,7002 WebLogic默认弱口令，反序列 
 
7778 Kloxo主机控制面板登录 
 
8000-9090 都是一些常见的web端口，有些运维喜欢把管理后台开在这些非80的端口上 
 
8080 tomcat/WDCP主机管理系统，默认弱口令 
 
8080,8089,9090 JBOSS 
 
8083 Vestacp主机管理系统 （国外用较多） 
 
8649 ganglia 
 
8888 amh/LuManager 主机管理系统默认端口 
 
9200,9300 elasticsearch 参考WooYun: 多玩某服务器ElasticSearch命令执行漏洞 
 
10000 Virtualmin/Webmin 服务器虚拟主机管理系统 
 
11211 memcache未授权访问 
 
27017,27018 Mongodb未授权访问 
 
28017 mongodb统计页面 
 
50000 SAP命令执行 
 
50070,50030 hadoop默认端口未授权访问
'''
#whois查询
#第三方库进whois查询也可以利用网上接口查
'''
from whois import Whois
w = Whois('google.com')
print(w)
'''
#子域名查询
#1.利用字典加载爆破进行查询
#2.利用bing或第三方接口进行查询


for  Subdomain in open('D:\safetools\dic.txt'):
    Su = Subdomain.replace('\n','')
    url = Su + '.'+'xueersi.com'
    try:
        ip=socket.gethostbyname(url)
        print(url+'->'+ip)
        time.sleep(0.01)
    except Exception as e:
        pass      
    




  