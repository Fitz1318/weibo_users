# weibo_users
Scrapy爬取新浪微博用户
将整个程序拷贝后只需运行main.py就可启动

通过分析[https://m.weibo.cn/](https://m.weibo.cn/)请求编写用户爬虫

用户信息保存到MongoDB

方法是先选取一个用户获取他的关注与粉丝

然后再分别获取他关注人和粉丝的关注与粉丝，以此类推

爬取时遇到了报403，所以禁用了cookies，且设置了延迟
```
COOKIES_ENABLED=False
DOWNLOAD_DELAY=1
```
还有一个随机更换`User-Agent`的中间件。


我本机抓了3W+还是正常运行
2018/4/10:这个程序是参考别人的，我会在此上面增加功能，加油！
