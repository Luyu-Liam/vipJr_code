# !/usr/bin/python
# coding: utf8
# @Author  : Liam
# @Email   : luyu.real@qq.com
# @Software: PyCharm

import requests

class TiebaSpider:
    def __init__(self, tiebaName):
        self.tiebaName = tiebaName
        self.url_temp = "http://tieba.baidu.com/f?kw=" + tiebaName + "&ie=utf-8&pn={}"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}

    def get_url_list(self, page_start, page_end):
        url_list = []
        for i in range(page_start, page_end+1):
            url_list.append(self.url_temp.format(i+50))
        return url_list

    def parse_url(self, url):
        print("正在爬取：{}".format(url))
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def save(self, html_str, page_num):
        filepath = "data/{}-第{}页".format(self.tiebaName, page_num)
        with open(filepath, "w", encoding="utf-8") as f:  # 杨超越-第4页.html
            f.write(html_str)



    def run(self, page_start, page_end):  # 实现主要逻辑
        # 1. 构造url列表
        url_list = self.get_url_list(page_start, page_end)
        # 2. 依次对url发送请求，获取响应数据
        for url in url_list:
            response = self.parse_url(url)
        # 3. 保存数据
            page_num = url_list.index(url) + page_start
            self.save(response, page_num)


if __name__ == '__main__':
    # spider_ycy = TiebaSpider("杨超越")
    # spider_ycy.run(20, 25)

    # 如何爬取一张图片？
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}
    img_url = "http://imgsrc.baidu.com/forum/w%3D580%3B/sign=ce9fe5bc01d79123e0e0947c9d0f5882/9c16fdfaaf51f3deb0900cd099eef01f3a297967.jpg"
    response = requests.get(img_url, headers=headers)
    with open("ycy2.jpg", "wb") as f:
        f.write(response.content)

