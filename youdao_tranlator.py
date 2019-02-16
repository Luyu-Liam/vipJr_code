# !/usr/bin/python
# coding: utf8
# Time: 2019-02-03 14:33
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import requests
from bs4 import BeautifulSoup


class youdao_trans:
    def __init__(self):
        self.url = "http://m.youdao.com/translate"
        self.headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 "
                                      "(KHTML, like Gecko) Chrome/70.0.3538.102 Mobile Safari/537.36"}

    def translate(self, content):
        response = self.parse(content)
        self.get_result(response)

    def parse(self, content):
        form_data = {
            'inputtext': content,
            "type": "AUTO"
        }
        response = requests.post(self.url, data=form_data, headers=self.headers)
        return response.content.decode()

    def get_result(self, response):
        soup = BeautifulSoup(response, "html.parser")
        try:
            res = soup.findAll(id='translateResult')[0].li.string
            print(res)
        except AttributeError:
            print("您操作过于频繁，请稍后操作")


if __name__ == '__main__':
    fanyi = youdao_trans()
    fanyi.translate("I love python")


