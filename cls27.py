# !/usr/bin/python
# coding: utf8
# @Author  : Liam
# @Software: PyCharm

import bs4
import requests

url = "https://so.gushiwen.org/mingju/"
req = requests.get(url)
soup = bs4.BeautifulSoup(req.text, "html.parser")
lst = soup.find_all("a", {"target": "_blank"})
with open('mingju.txt', 'w', encoding='utf-8') as f:
    for i in range(len(lst) - 1):
        s = str(lst[i + 1])
        res = s[s.find("\">") + 2: s.find("</")]
        f.write(res)
        if i % 2 == 0:
            f.write('---')
        else:
            f.write('\n')
        print(res, end=("---" if i % 2 == 0 else "\n"))



