#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import urllib2
from lxml import etree
import re,sys,os,requests

#设置编码格式
reload(sys)
sys.setdefaultencoding('utf-8')
#获得系统编码格式
type = sys.getfilesystemencoding()


def request_url(url): 
	'''
		#request请求，返回unicode格式
	'''
	try:
		headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"} 
		response = requests.get(url,headers = headers)
		res = response.text	
		return res
	except Exception as error:  
		print error  

def requestImage(url):
	'''
		作用：request请求，返回字节流，用来保存图片  

	'''
	try:  
		headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
		response = requests.get(url,headers = headers).content
		return response
	except Exception as error:  
		print error       

def loadPage(url):
    """
        作用：根据url发送请求，获取服务器响应文件
        
    """
    html = request_url(url)

    if html == '':
    	print raw_input(unicode("Error,请求失败！",'utf-8').encode(type)) #request请求错误
        return
    # 解析HTML文档为HTML DOM模型
    content = etree.HTML(html)

    # 返回 图片url和图下面的名字字符串
    link_list = content.xpath('//div[@class="c cl"]/a/img/@src')
    name_list = content.xpath('//div[@class="c cl"]/a/img/@alt')

    for index,link in enumerate(link_list):
        #rint index,link
        print str(int(index)+1)
        # 组合为每个帖子的链接
        fulllink = homeurl + link
        #取出名字
        name = name_list[index]
        writeImage(fulllink,name)


# 取出每个帖子里的每个图片连接
def loadhomepage(url, kw, beginPage, endPage):
	#请求
    html = request_url(url)
    
    if html == '':
    	print raw_input(unicode("Error,请求失败！",'utf-8').encode(type)) #request请求错误
        return

    # 解析
    content = etree.HTML(html)
    # 取出帖子里关键字 { 需要注意的是最后加一个text() }
    name_xpath = '//li[@onmouseover="this.className='+"'lihover cl'"+'"]/dl/a/span/text()'
    item_name = content.xpath(name_xpath)
    # 取出帖子里链接
    link_xpath =  '//li[@onmouseover="this.className='+"'lihover cl'"+'"]/dl/a/@href'
    link_list = content.xpath(link_xpath)

    newlist = []
    for name in item_name:
    	keyname = name.decode("utf-8","ignore").encode("gbk","ignore")
    	
    	newlist.append(keyname)

    if kw in newlist:
    	
    	index = newlist.index(kw)
    	
        link = link_list[index]
        
        newlink = url+link  #进入板块
        tiebaSpider(newlink, beginPage, endPage)
    else:
        print raw_input(unicode("Error,输入需要爬取的关键字不存在！",'utf-8').encode(type)) #关键字kw
    


def writeImage(link,name):
    """
        作用：将html内容写入到本地
        link：图片连接
    """
    #print link
    image = requestImage(link)

    if image == '':
    	print raw_input(unicode("Error,请求失败！",'utf-8').encode(type)) #request请求错误
    	return
    list_str = name.split()
    print list_str[0]
    filename = list_str[0]+'.jpg'
    # 写入到本地磁盘文件内
    with open(filename, "wb") as f:
        f.write(image)
    #print unicode("已经成功下载 ",'utf-8').encode(type)+filename

def tiebaSpider(newlink, beginPage, endPage):  #, beginPage, endPage
    """
        作用：爬去每一页图片
        
    """
    #print newlink

    for page in range(beginPage, endPage + 1):
        pn = page
        #filename = "第" + str(page) + "页.html"
        fullurl = newlink + "&page=" + str(pn)
        #print fullurl
        loadPage(fullurl)
        #print html

        print str(page)+" page "+' end!'

    

if __name__ == "__main__":
    kw = raw_input(unicode("请输入需要爬取的关键字: ",'utf-8').encode(type)) #关键字kw
    beginPage = int(raw_input(unicode("请输入起始页：",'utf-8').encode('gbk')))
    endPage = int(raw_input(unicode("请输入结束页：",'utf-8').encode('gbk')))
    homeurl = "https://www.cheshenluntan12.com/"  #主页
    loadhomepage(homeurl, kw, beginPage, endPage)






