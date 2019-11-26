作者：何强

邮箱：1422127065@qq.com

**python高级之初识socket网络编程**

简单实现服务端和客户端之间的通信

首先创建一个server.py

```python
import socket

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=8888
server.bind((host,port))
server.listen()
while True:
    socket,addr=server.accept()
    # 获取从客户端发送的数据
    # 一次获取1k的数据
    # data为byte类型
    data=socket.recv(1024)#接收来自客户端的信息
    #发送的信息必须是byte类型  这里是发送到客户端的信息
    socket.send("hello {}".format(data.decode("utf8")).encode("utf-8"))
    print(data.decode("utf8"))
    print(addr)#打印地址
    socket.close()

```



接着创建一个client段 

client.py

```python
import socket
import sys
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8888
# 连接服务，指定主机和端口
client.connect((host, port))

client.send("ceshi".encode("utf-8"))
# 接收小于 1024 字节的数据 这里接收的是来自服务端的数据
msg = client.recv(1024)
client.close()
print(msg.decode("utf8"))
```

先运行 server.py  控制台会处于等待状态

接着运行 client.py发送数据

client.py 

#output   

hello ceshi



server.py 

#output   

客户端可多次运行查看服务端打印数据



这里不对socket理论不做过多的赘述

有兴趣可以看一下 https://www.cnblogs.com/yunlong-study/p/9283529.html 

