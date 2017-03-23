import socket
import sys

# 创建socket 对象

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

# 端口
port = 9999

# 连接服务，指定主机和端口
clientSocket.connect((host, port))

# 接收数据
msg = clientSocket.recv(1024)

clientSocket.close()

print('clientSocket: ', msg.decode('utf-8'))
