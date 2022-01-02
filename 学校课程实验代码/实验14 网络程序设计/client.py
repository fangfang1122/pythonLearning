# 客户端
import socket
# 声明socket的链接类型
client = socket.socket()
# 连接一个地址和端口
client.connect(('localhost', 6969))
#发送bytes数据类型的数据
client.send(b"hello word")
# 接收服务器端发送过来的数据
data = client.recv(1024)
print("服务器端发送回来的数据：",data)
client.close()