# !/usr/bin/python
# coding: utf8
# Time: 2018-12-29 22:38
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm

import requests
from bs4 import BeautifulSoup
import os

"""
爬取笔趣阁小说
"""
class BiquyunSpider:
    def __init__(self, url):
        self.url = url
        self.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}


    def get_bookname(self):
        """获取小说名称"""
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content.decode("gbk"), features='html.parser')
        bookName = soup.find("div", id="info").h1.text
        return bookName


    def get_text(self, url):
        """获取每一章节的内容"""
        response = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(response.content.decode('gbk'), features='html.parser')
        result = soup.find_all("div", id="content")[0].text.replace("\xa0"*4, "\n\n")
        return result


    def find_chapters(self):
        """获取每个章节的url和章节标题"""
        chapters = {}   # 字典保存每个章节的信息，key存放的是章节标题，value存放的是对应章节的url
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content.decode('gbk'), features='html.parser')
        result = soup.find_all("div", id='list')[0].dl
        for item in result:
            try:
                tmp_url = "http://www.biquyun.com" + item.a.get('href')  # 拼接得到完成的章节url
                chapters[item.a.string] = tmp_url
                # print(tmp_url)
            except AttributeError:  # 有可能a标签不存在，导致异常，这里可以不做处理
                pass
        return chapters


    def download_novels(self):
        """主逻辑，完成小说的下载与保存"""
        bookName = self.get_bookname()
        os.mkdir(bookName)  # 以书名作为文件夹的名称创建文件夹，用以存放该小说
        chapters = self.find_chapters()
        for title, url in chapters.items():
            content = self.get_text(url)
            print("正在下载：" + title)
            with open(os.path.join(bookName, title+".txt"), "w") as f:
                f.write(content)


if __name__ == '__main__':
    url = "http://www.biquyun.com/2_2027/"
    doupo = BiquyunSpider(url)
    doupo.download_novels()
