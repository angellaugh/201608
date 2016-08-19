# -*- coding=utf-8 -*-
import http.client
import urllib2
url_save = 'http://www.baidu.com'

try:
	s_save = urllib2.urlopen(url_save).read()
	print(s_save)
except urllib2.URLError,e:
	print(e.code)
except urllib2.URLError,e:
	print(str(e))