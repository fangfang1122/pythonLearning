"""
（一）编写程序实现服务器端的自动发现功能。服务器程序运行后，每隔1s向局域网内所有计算机发送信息ServerIP，
局域网内所有计算机接收信息之后，获取并输出服务端IP地址。
"""
# 没做出来
import socket
import threading
import time

activeDegree = dict()
flag = 1


def main():
    global activeDegree
    global flag
    HOST = socket.gethostbyname(socket.gethostname())
    print(socket.IPPROTO_IP)
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    s.bind((HOST, 0))
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    while flag:
        c = s.recvfrom(65565)
        host = c[1][0]
        activeDegree[host] = activeDegree.get(host, 0) + 1
        s.connect((host, c[1][1]))
        s.sendall(b"hello word")
        if c[1][0] != '127.0.0.1':
            print(c)
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
    s.close()


t = threading.Thread(target=main)
t.start()
time.sleep(60)
flag = 0
t.join()
for item in activeDegree.items():
    print(item)
