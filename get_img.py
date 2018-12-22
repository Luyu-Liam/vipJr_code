# !/usr/bin/python
# coding: utf8
# Time: 2018-12-22 01:04
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import requests
import bs4

def parse_and_save(url, name):
    response = requests.get(url)
    name += ".png"
    with open(name, "wb") as f:
        f.write(response.content)


url = "https://www.taptap.com/topic/3142024?from=bdcambrian"
response = requests.get(url)
parser_only = bs4.SoupStrainer(class_="bbcode-img")
soup = bs4.BeautifulSoup(response.content.decode(), "html.parser", parse_only=parser_only)
url_list = []
index = 1
for i in soup:
    name = "pic" + str(index)
    parse_and_save(i.get('data-origin-url'), name)
    index += 1
