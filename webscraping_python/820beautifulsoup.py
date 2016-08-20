__author__ = 'vivi'

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsobj = BeautifulSoup(html, "html.parser")
namelist = bsobj.findAll("span", {"class": "green"})
for name in namelist:
    print(name.get_text())      # get_text()清除所有标签，返回只包含文字的字符串

contentlist = bsobj.findAll("span", {"class": {"green", "red"}})  # 标签和属性值都可以是多个
for content in contentlist:
    print(content.get_text())

textlist = bsobj.findAll(text="the prince")
# for text1 in textlist:
#     print(text1.get_text())
print(len(textlist))

allText = bsobj.findAll(id="text")
print(allText[0].get_text())





# ------------------------------------------------------------
shopingweb = urlopen("http://www.pythonscraping.com/pages/page3.html")
shopingobj = BeautifulSoup(shopingweb, "html.parser")

for child in shopingobj.find("table", {"id": "giftList"}).children:
    print(child)
    print("end!!!!")

# 后代报错了
# for descenda in shopingobj.find("table", {"id", "giftList"}).descendants:
#     print(descenda)

# 表格也报错了
# for sibling in shopingobj.find("table", {"id": "giftLsit"}).tr:
#     print(sibling)

# 父标签 估计不会使用
print(shopingobj.find("img", {"src": "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())


# BeautifulSoup & re 和正则的结合

import re

imges = shopingobj.findAll("img", {"src": re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
for image in imges:
    print(image["src"])


