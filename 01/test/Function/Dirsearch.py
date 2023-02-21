import sys
import os
import queue
import random

import requests
import time
import threading

# q = queue.Queue()

#
# def scan():
#     while not q.empty():  ### 只要字典里不为空，就一直循环
#         dir = q.get()  ### 把存储的payload取出来
#         urls = url + dir  ### url+payload就是一个payload
#         urls = urls.replace('\n', '')  ### 利用回车来分割开来，不然打印的时候不显示
#         code = requests.get(urls).status_code  ### 把拼接的url发起http请求
#         if code == 200 or code == 403:  ### 如果返回包状态码为200或者403，就打印url+状态码
#             print(urls + '|' + str(code))
#             f = open('ok.txt', 'a+')  ###然后把结果以追加的方式存储到ok.txt中，然后关闭文件
#             f.write(urls)
#             f.close()
#
#         else:
#             print(urls + '|' + str(code))
#             time.sleep(1)
#             ### 不然就打印url+状态码，并延时一秒

def Scan(url,dir):
    dir_list = open_dir_txt(dir)
    for i in dir_list:
        time.sleep(random.random())
        urls = url+"/"+i
        code = requests.get(url=urls).status_code
        if code == 200 or code == 403:
            print(urls + "-------" + str(code))


def open_dir_txt(filename):
    url_list = []
    with open(filename, 'r') as f:
        for l in f:
            url_list.append(l.strip())
    return url_list




if __name__ == '__main__':
    path = os.path.dirname(os.path.realpath(__file__))  ### 这里的功能是获取当前的路径
    url = sys.argv[1]  ### 用户输入的url
    txt = sys.argv[2]  ### 用户输入的字典
    xc = sys.argv[3]  ### 用户输入的线程
    for dir in open(path + "/" + txt):
        q.put(dir)
        ### 当前路径加上字典名就是绝对路径，然后循环字典里的payload
    for i in range(int(xc)):
        t = threading.Thread(target=scan)
        t.start()

        ### 多线程实现