作者：何强

邮箱：1422127065@qq.com

**python 高级初识socket网络编程**

简单实现服务端和客户端之间的通信 实现多人聊天

首先创建一个server.py

```python
import socket
import threading

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=8888
server.bind((host,port))
server.listen()
def handle_socket(sock,addr):
    while True:
        client_data=sock.recv(1024)
        print(client_data.decode("utf8"))
        new_data = input("请输入聊天信息\n")
        sock.send(new_data.encode("utf8"))
while True:
    # 获取从客户端发送的数据
    # 一次获取1k的数据
    # data为byte类型
    sock, addr = server.accept()
    # 多线程实现多人聊天
    client_threde=threading.Thread(target=handle_socket,args=(sock,addr))
    client_threde.start()



```



接着创建一个client端

client.py

```python
import socket
import sys
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8888
# 连接服务，指定主机和端口
client.connect((host, port))

while True:
    client_data = input("请输入你的聊天信息\n")
    client.send(client_data.encode("utf8"))
    server_data = client.recv(1024)
    print(server_data.decode("utf8"))

```

先运行 server.py  控制台会处于等待状态

接着运行 client.py发送数据



利用多线程实现多个客服端的连接 实现多人聊天模式

每次运行一个客户端都会开启一个新的线程



这里不对socket理论不做过多的赘述



