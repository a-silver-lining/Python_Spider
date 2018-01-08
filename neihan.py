#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2
import re
import re,sys,os
from lxml import etree
#设置编码格式
reload(sys)
sys.setdefaultencoding('utf-8')
#获得系统编码格式
type = sys.getfilesystemencoding()


class Spider:
    def __init__(self):
        # 初始化起始页位置   url = "http://www.neihan8.com/article/index_2.html"
        self.page = 1
        # 爬取开关，如果为True继续爬取
        self.switch = True

    def loadPage(self):
        """
            作用：下载页面
        """
	if self.page == 1:
		url = "http://www.neihan8.com/article/"
	else:
		url = "http://www.neihan8.com/article/index_" + str(self.page) + ".html"
		print url+"    ---------"
        headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
        request = urllib2.Request(url, headers = headers)
        response = urllib2.urlopen(request)

        # 获取每页的HTML源码字符串
        html = response.read()
        
        text = etree.HTML(html)

        content_list = text.xpath('//div[@class="text-column-item box box-790"]/div[@class="desc"]/text()')

        # 调用dealPage() 处理段子里的杂七杂八
        self.dealPage(content_list)

    def dealPage(self, content_list):
        """
            处理每页的段子
            content_list : 每页的段子列表集合
        """
        for item in content_list:
            # 将集合里的每个段子按个处理，替换掉无用数据
            item = item.replace("<p>","").replace("</p>", "").replace("<br>", "")
            
            # 处理完后调用writePage() 将每个段子写入文件内
            self.writePage(item)

    def writePage(self, item):
        """
            把每条段子逐个写入文件里
            item: 处理后的每条段子
        """
        # 写入文件内
        print unicode("正在写入数据....",'utf-8').encode('gbk')
        with open("duanzi.txt", "a") as f:
            f.write(item+"\n")
			

    def startWork(self):
        """
            控制爬虫运行
        """
        # 循环执行，直到 self.switch == False
        while self.switch:
            # 用户确定爬取的次数
            self.loadPage()
            command = raw_input(unicode("如果继续爬取，请按回车（退出输入quit)",'utf-8').encode('gbk'))
            if command == "quit":
                # 如果停止爬取，则输入 quit
                self.switch = False
            # 每次循环，page页码自增1
            self.page += 1
        print unicode("谢谢使用！",'utf-8').encode('gbk')


if __name__ == "__main__":
    duanziSpider = Spider()
    duanziSpider.startWork()

