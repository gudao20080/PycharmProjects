import socket
import sys

# 创建socket对象
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 本地主机名
host = socket.gethostname()

port = 9999

# 绑定端口
serverSocket.bind((host, port))

# 设定最大连接数
serverSocket.listen(8)

while True:
    # 建立客户端连接
    clientSocket, addr = serverSocket.accept()

    print("连接地址：{}".format(str(addr)))

    msg = '欢迎欢迎： \r\n'
    clientSocket.send(msg.encode('utf-8'))
    clientSocket.close()



