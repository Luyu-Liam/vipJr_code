# !/usr/bin/python
# coding: utf8
# @Time    : 2018-12-20 10:36
# @Author  : Liam
# @Email   : luyu.real@qq.com
# @Software: PyCharm
from bs4 import BeautifulSoup, NavigableString, SoupStrainer


html_doc = """" 
<html>
    <head><title>The Dormouse‘s story</title></head>
    <body> 
        <p class=“title”><b>The Dormouse‘s story</b></p> 
        <p class=“story”>
            Once upon a time there were three little sisters; and their names were: 
            <a href=“http://example.com/elsie” class="sister" id="link1" >Elsie</a>, 
            <a href=“http://example.com/lacie” class="sister" id="link2" >Lacie</a> and 
            <a href=“http://example.com/tillie” class="sister" id="link3" >Tillie</a>,
            and they lived at the bottom of a well.</p> 
        <p class=“story”>...</p> 
    </body>
"""

"""爬虫的使用方法 1"""
soup = BeautifulSoup(html_doc, "html.parser")   # BeautifulSoup对象
head_tag = soup.head   # BeautifulSoup的属性也是一个对象，这里是Tag对象
# print(head_tag)

# Tag可以一层一层往下调
b_tag = soup.p.b
# print(b_tag)

# 获取所有的标签，以a标签为例
a_tags = soup.find_all("a")
# print(a_tags, type(a_tags))

# tag的.contents属性可以将tag的子标签以列表的形式输出
# print(soup.body.contents, len(soup.body.contents))

# tag的.children属性可以将tag的子标签生成一个可迭代对象，采用循环的方式取出
# p_children = soup.body.children
# for child in p_children:
#     print(child)

# tag的.descendants属性可以将tag的后代生成一个可迭代对象
# p_descendants = soup.body.descendants
# for descendant in p_descendants:
#     print(descendant)

# 把上面html字符串中的“story”打印出来
# s = soup.body.contents[3]
# st = ""
# for i in s.descendants:
#     # print(i, type(i))
#     # print("*"*44)
#     if type(i) == NavigableString:
#         st += i
# st = st.replace("\n", "").replace("  ", '')
# print(st)

# 当tag中只有一个NavigableString类型的子节点时，可以用string方法将其获得. 注意换行符去掉
# title_tag = head_tag.contents
# title_tag = head_tag.string
# print(title_tag)


# strings方法可以获取tag子节点中的所有NavigableString类型的内容，可用循环取出，下面是上节课作业的另一种写法
# s = soup.body.contents[3]
# st = ''
# for item in s.strings:
#     st += item
#
# st = st.replace("\n", '').replace("  ", "")
# print(st)


# strpped_strings可以获取当前tag中的string子节点，并且自动帮助我们去掉多余的空白字符
# s = soup.body.contents[3]
# st = ''
# for item in s.stripped_strings:
#     st += item
# print(st)


# parent方法可以获取当前tag的父节点
# title_tag = soup.title
# print(title_tag)
# print(title_tag.parent)


# parents可以递归得到该元素的所有父辈节点
# link = soup.a
# print(link)
# for item in link.parents:
#     print(item.name)


# prettify()方法可以让html文档以一种树形结构显示
# print(soup.prettify())


# 下面的方法可以获取兄弟节点，但要注意把换行符算在内
# print(soup.head.next_sibling)
# print(soup.body.previous_sibling)


# next_siblings和previous_siblings可以将当前节点的兄弟节点迭代输出
# for sibling in soup.a.next_siblings:
#     print(repr(sibling))
#     print("*"*88)


# print(soup.find('b'))
# print(soup.find_all(['a', 'b']))

# 自定义过滤器
# def has_class_but_no_id(tag):
#     return tag.has_attr('class') and not tag.has_attr('id')
# print(soup.find_all(has_class_but_no_id))

# print(soup.find_all(id="link2"))
# print(soup.find_all('a', class_='sister'))
# print(soup.find_all('a', class_='sister', limit=2))

# recursive参数
# print(soup.find_all('a'))
# print(soup.find_all('a', recursive=False))


# 把三姐妹的名称打印出来
# for i in soup.find_all('a'):
#     print(i.text)

# for i in soup.find_all("a"):
#     print(i.string)


# CSS选择器
# print(soup.select(".sister"))


# print(soup.body.get_text())

# only_a_tag = SoupStrainer("a")
# print(BeautifulSoup(html_doc, "html.parser", parse_only=only_a_tag).prettify())


# 爬取古诗名句
import requests
url = "https://so.gushiwen.org/mingju/"
response = requests.get(url)
find_range = SoupStrainer(style=" float:left;")
soup = BeautifulSoup(response.content.decode(), "html.parser", parse_only=find_range)
index = 0
for item in soup.strings:
    print(item, end='-----' if index%2==0 else "\n")
    index += 1

# 如何获取链接呢?
link_list = []
find_range2 = SoupStrainer(style=" width:44px;")
soup2 = BeautifulSoup(response.content.decode(), "html.parser", parse_only=find_range2)
for item in soup2:
    link_list.append(item.get('href'))
print(link_list)

