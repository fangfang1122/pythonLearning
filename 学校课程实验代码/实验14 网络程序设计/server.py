# 服务器端
import socket

# 声明链接类型
server = socket.socket()
# 绑定一个网卡和选择端口
server.bind(('0.0.0.0', 6969))
# 开始监听
server.listen()
# 开始等待请求(conn为客户端发送的请求在服务器端生成的连接实例，addr为请求的地址以及端口号)
print("等待请求")
conn, addr = server.accept()
print("收到请求")
# 接收数据
data = conn.recv(1024)
print("从客户端接收到的数据：", data)
# 返回处理好的数据
conn.send(data.upper())
server.close()