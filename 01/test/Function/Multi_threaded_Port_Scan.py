#coding:utf-8

import socket
from datetime import datetime
from multiprocessing.dummy import Pool as ThreadPool



def scan_port(port):
    try:
        s = socket.socket(2,1) #2:socket.AF_INET 1:socket.SOCK_STREAM
        #AF_INET代表ipv4，SOCK_STREAM代表流式socket，对于发送的是TCP请求
        #其实这两个参数不写也没事，因为默认的就是AF_INET和SOCK_STREAM
        res = s.connect_ex((remote_server_ip,port))#连接到address处的套接字，参数为元组格式。有返回值，连接成功时返回0，出错时返回错误编码

        if res == 0: # 如果端口开启
            print('Port %s: OPEN' % port)
        s.close()#关闭套接字

    except Exception as e:
        print(str(e.message))



if __name__ == '__main__':
    remote_server_ip = input('输入要扫描的IP：')
    ports = []

    socket.setdefaulttimeout(0.5)  # 设置超时为0.5秒

    for i in range(1, 65536):  # 全端口扫描
        ports.append(i)

    # Check what time the scan started
    t1 = datetime.now()
    pool = ThreadPool(processes=1000)  # 设置线程池为1000
    results = pool.map(scan_port, ports)
    print(results)
    pool.close()
    pool.join()

    print('Multiprocess Scanning Completed in  %s' % (datetime.now() - t1))