from ftplib import FTP         #引入ftp模块
import os

host = "39.107.241.226"
port = 21  # not str
username = "ftpuser"
password = "btbu2018"
ftp = FTP()       #设置ftp服务器地址
ftp.connect(host, port)
ftp.login(user=username, passwd=password)      #设置登录账户和密码

localfile = 'C:\工作\zhu13818202655.github.io\img\photo1.jpg'    #设定文件位置
f = open(localfile, 'rb')        #打开文件
#file_name=os.path.split(localfile)[-1]
#ftp.storbinary('STOR %s'%file_name, f , 8192)
ftp.storbinary('STOR %s' % os.path.basename(localfile), f) #上传文件