# -*- coding: utf-8 -*-
import urllib2
import cookielib
# urlopen(url, data, timeout)
# data默认为空None，timeout默认为 socket._GLOBAL_DEFAULT_TIMEOUT
# response = urllib2.urlopen("http://www.zhihu.com")
# print response.read()

# 构造request
request = urllib2.Request("http://www.zhihu.com")
response = urllib2.urlopen(request)
print response.read()

# urllib2 默认会使用环境变量 http_proxy 来设置 HTTP Proxy
# enable_proxy = True
# proxy_handler = urllib2.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
# null_proxy_handler = urllib2.ProxyHandler({})
# if enable_proxy:
#     opener = urllib2.build_opener(proxy_handler)
# else:
#     opener = urllib2.build_opener(null_proxy_handler)
# urllib2.install_opener(opener)

# cookielib模块的主要作用是提供可存储cookie的对象，以便于与urllib2模块配合使用来访问Internet资源
# 声明一个CookieJar对象实例来保存cookie
# cookie = cookielib.CookieJar()
# # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
# handler=urllib2.HTTPCookieProcessor(cookie)
# # 通过handler来构建opener
# opener = urllib2.build_opener(handler)
# # 此处的open方法同urllib2的urlopen方法，也可以传入request
# response = opener.open('http://www.zhihu.com')
# for item in cookie:
#     print 'Name = '+item.name
#     print 'Value = '+item.value

# # 保存Cookie到文件
# # 设置保存cookie的文件，同级目录下的cookie.txt
# filename = 'cookie.txt'
# # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
# cookie = cookielib.MozillaCookieJar(filename)
# # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
# handler = urllib2.HTTPCookieProcessor(cookie)
# # 通过handler来构建opener
# opener = urllib2.build_opener(handler)
# # 创建一个请求，原理同urllib2的urlopen
# response = opener.open("http://www.zhihu.com")
# # 保存cookie到文件
# cookie.save(ignore_discard=True, ignore_expires=True)
# # ignore_discard: save even cookies set to be discarded.
# # ignore_expires: save even cookies that have expiredThe file is overwritten if it already exists

# 创建MozillaCookieJar实例对象
# cookie = cookielib.MozillaCookieJar()
# 从文件中读取cookie内容到变量
# cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# 创建请求的request
# req = urllib2.Request("http://www.zhihu.com")
# 利用urllib2的build_opener方法创建一个opener
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# response = opener.open(req)
# print response.read()