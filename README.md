# Python_Spider
初级爬虫
# Python_Spider
这是Python爬虫项目,持续更新中.......

项目介绍：
1、newcar.py
爬取得网址：www.cheshenluntan12  爬取图片示例。

爬取的是车神论坛的image

使用者需要输入的项：项目名（例如：女教师）以及爬取的起止页数beginpage和endpage

保存的image命名是番号，保存地址是与newcar.py相同路径下

爬虫主要用到的是lxml和requests这两个模块，车神论坛地址有可能变，请使用者确认网址是否正确


2、baidutieba_imagespider.py

爬取的是百度贴吧的图片：使用者只需输入想爬的贴吧名以及起止页数，例如美女吧，1页到2页，项目就会爬取各楼层发的美照！

项目主要用到了lxml，用户需要自己下载安装

爬取的图片保存在本地

3、douban_spilder.py
爬取的是 豆瓣电影分类排行榜 - 剧情片  前二十项

豆瓣http的请求方式是post，我们需要抓包工具（例如Fiddler）抓包，观察请求和响应的地址，由于豆瓣后台采用的是ajax异步加载，而且返回的数据是json格式，我们将数据以json格式保存在本地，即movie.json, 并且此项目使用了代理服务器，免费的代理来源：快代理ip

4、neihan.py 
爬取的是内涵段子吧的主页贴子里面的段子

每爬取一页上的数据时，询问用户控制是否接着爬取下一页内容，确认敲回车，退出quit

主要用的是lxml和urllib2的request