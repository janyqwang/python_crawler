# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

# urllib2 默认会使用环境变量 http_proxy 来设置 HTTP Proxy
# enable_proxy = True
# proxy_handler = urllib2.ProxyHandler({"http":'http://some-proxy.com:8080'})
# null_proxy_handler = urllib2.ProxyHandler({})
# if enable_proxy:
#     opener = urllib2.build_opener(proxy_handler)
# else:
#     opener = urllib2.build_opener(null_proxy_handler)
# urllib2.install_opener(opener)
#
class qiubai:
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        # initialize headers
        self.headers = {'User-Agent': self.user_agent}
        self.stories = []
        self.enable = False

    def getPage(self,pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            request = urllib2.Request(url, headers = self.headers)
            response = urllib2.urlopen(request)
            pageCode = response.read().decode('utf-8', 'ignore')
            return pageCode
            # print response.read()
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print e.code
            if hasattr(e, "reason"):
                print e.reason
        # [Errno 11004] getaddrinfo failed 访问了一个不存在的网址（因为用了上面的代理)
    def getPageItems(self,pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print "Failed to get page..."
            return None
        # pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?' + 'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>', re.S)
        # pattern = re.compile('<div.*?author.*?>.*?<img.*?>.*?<h2>(.*?)</h2>.*?<div.*?' + 'content>(.*?)</div>(.*?)<div class=stats.*?class=number>(.*?)</i>', re.S)
        pattern = re.compile('h2>(.*?)</h2.*?content">(.*?)</.*?number">(.*?)</', re.S)
        items = re.findall(pattern, pageCode)
        pagestories = []
        for item in items:
            # haveImg = re.search("img", item[3])
            # if not haveImg:
            pagestories.append([item[0], item[1], item[2]])
        return pagestories

    def loadPage(self):
        if self.enable == True:
            if len(self.stories)<2:
                pagestories = self.getPageItems(self.pageIndex)
                if pagestories:
                    self.stories.append(pagestories)
                    self.pageIndex += 1

    def getOneStory(self,pagestories,page):
        for story in pagestories:
            input = raw_input()
            self.loadPage()
            if input == "q":
                self.enable = False
                return
            print "Page %d\tAuthor:%s\tThumb:%s\n%s"%(page, story[0], story[2],story[1])

    def start(self):
        print "Push Enter to start...q to quit"
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.stories)>0:
                pagestories = self.stories[0]
                nowPage += 1
                del self.stories[0]
                self.getOneStory(pagestories, nowPage)
# spider = qiubai()
# spider.start()

if __name__ == '__main__':
    qb = qiubai()
    qb.start()