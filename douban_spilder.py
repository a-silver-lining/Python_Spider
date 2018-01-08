#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import urllib2
import re,sys,os,json

#设置编码格式
reload(sys)
sys.setdefaultencoding('utf-8')
#获得系统编码格式
type = sys.getfilesystemencoding()

'''
	豆瓣电影分类排行榜 - 剧情片

'''

#这个地址post请求地址，需要抓包工具（例如Fiddler）进行抓包
url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action"

# 代理开关，表示是否启用代理
proxyswitch = False

# 构建一个Handler处理器对象，参数是一个字典类型，包括代理类型和代理服务器IP+PROT
httpproxy_handler = urllib2.ProxyHandler({"http" : "60.214.154.2:53281"})

# 构建了一个没有代理的处理器对象
nullproxy_handler = urllib2.ProxyHandler({})

if proxyswitch:
    opener = urllib2.build_opener(httpproxy_handler)
else:
    opener = urllib2.build_opener(nullproxy_handler)

# 构建了一个全局的opener，之后所有的请求都可以用urlopen()方式去发送，也附带Handler的功能
urllib2.install_opener(opener)

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

formdata = {
        "start":"0",
        "limit":"20"
    }

def writePage(json, filename):
    """
        作用：将html内容写入到本地
        html：服务器相应文件内容
    """
    print unicode("正在保存 ",'utf-8').encode('gbk') + filename
    # 文件写入
    with open(filename, "w") as f:
        f.write(json)
    print "-" * 30
	
data = urllib.urlencode(formdata)

request = urllib2.Request(url, data = data, headers = headers)

#print urllib2.urlopen(request).read().decode('utf-8').encode(type)
response = urllib2.urlopen(request).read().decode('utf-8').encode(type)

writePage(response,'movies.json')




