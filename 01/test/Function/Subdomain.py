import requests                      
 #BS主要功能是从网页抓取数据，提供一些简单的、python 式的函数用来处理导航、搜索、修改分析树等功能
from bs4 import BeautifulSoup  
#模块主要用于解析url中的参数，对url按照一定格式进行 拆分或拼接，将url分为6个部分，返回一个包含6个字符串项目的元组：协议、位置、路径、参数、查询、片段     
from urllib.parse import urlparse   
import sys 

def bing_search(site,pages):
    Subdomain = []
    headers = {        
        'User-Agent': 'Mozilla/5.0 (x11; Linux x86_64;rv:68.0)Gecko/20100101 Firefox/68.0',   
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Referer': "https://cn.bing.com", 
        'Cookie': ""   
    }
    for i in range(1,int(pages)+1):
        url = "https://cn.bing.com/search?q=site%3a"+site+"&go=Search&qs=ds&first="+ str((int(i)-1)*10) +"&FORM=PERE"
        html = requests.get(url,headers=headers)     #获取HTML网页，对应HTTP的GET
        soup = BeautifulSoup(html.content,'html.parser')
        job_bt = soup.findAll('h2')     #返回一个包含HTML文档标题标签h2的列表
        for i in job_bt:
            link = i.a.get('href')
            domain = str(urlparse(link).scheme + "://" +urlparse(link).netloc)  #储存子域名
            if domain in Subdomain:
                pass
            else:
                Subdomain.append(domain)
                print(domain)
if __name__ == '__main__':
    if len(sys.argv) == 3:
        site = sys.argv[1]
        page = sys.argv[2]
    else:
        print("usage: %s baidu.com 10" % sys.argv[0])         #输出帮助信息
        sys.exit(0)
    Subdomain = bing_search(site,page)