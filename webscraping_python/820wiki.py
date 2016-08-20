__author__ = 'vivi'
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

wikiurl = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
wikiobj = BeautifulSoup(wikiurl, "html.parser")
print(wikiobj)
# 打印所有a标签下的链接内容
for link in wikiobj.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])
# 打印wiki开头，不带冒号，在div里id是bodyContent的链接
for linkre in wikiobj.find("div", {"id": "bodyContent"}).findAll("a", href = re.compile("^(/wiki)((?!:).)*$")):
    if 'href' in linkre.attrs:
        print(linkre.attrs['href'])
print("Kevin is Over,and Lishizhen is beginning")
# ------------------------------------------------------------------
import datetime
import random

random.seed(datetime.datetime.now())
def getlinks(articleUrl):
    wikipediaurl = urlopen("http://en.wikipedia.org"+ articleUrl)
    wikipeidaobj = BeautifulSoup(wikipediaurl, "html.parser")
    return wikipeidaobj.find("div", {"id": "bodyContent"}).findAll("a", href = re.compile("^(/wiki/)((?!:).)*$"))
findlinks = getlinks("/wiki/Li_Shizhen")
while len(findlinks) > 0:
    newArticle = findlinks[random.randint(0, len(findlinks)-1)].attrs["href"]
    print(newArticle)
    findlinks = getlinks(newArticle)