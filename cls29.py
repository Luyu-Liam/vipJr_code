# !/usr/bin/python
# coding: utf8
# @Author  : Liam
# @Email   : luyu.real@qq.com
# @Software: PyCharm
import requests
import json


"""
有关json用法的练习
"""
# url = "https://fanyi.baidu.com/basetrans"
# headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Mobile Safari/537.36"}
# data = {
#             'query': 'Life is short, use python',
#             'from': 'en',
#             'to': 'zh'
#         }
# response = requests.post(url, data=data, headers=headers)
# json_str = response.content.decode()
# print(json_str)

# json.loads把json字符串转换为python类型
# ret1 = json.loads(json_str)
# print(ret1)


# json.dumps把python类型转换为json字符串
# with open('translator.json', 'w', encoding='utf-8') as f:
#     f.write(json.dumps(ret1, ensure_ascii=False, indent=4))

# with open('translator.json', 'r', encoding='utf-8') as f:
#     ret2 = f.read()
#     ret3 = json.loads(ret2)
#     print(ret3)
#     print(type(ret3))

# 使用json.load()提取类文件对象中的数据
# with open('translator.json', 'r', encoding='utf-8') as f:
#     ret4 = json.load(f)
#     print(ret4)
#     print(type(ret4))

# 使用json.dump()能够把python类型放入类文件对象中
# with open('translator1', 'w', encoding='utf-8') as f:
#     json.dump(ret1, f, ensure_ascii=False, indent=4)



"""
百度翻译小爬虫
"""
class Translator:
    def __init__(self, query_str):
        self.langdetect_url = "https://fanyi.baidu.com/langdetect"
        self.langdetect_data = {"query": query_str}
        self.query_str = query_str
        self.post_url = "https://fanyi.baidu.com/basetrans"
        self.headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Mobile Safari/537.36"}

    def zh_or_en(self):
        langdetect_response = requests.post(self.langdetect_url, headers=self.headers, data=self.langdetect_data)
        lang = json.loads(langdetect_response.content.decode())['lan']
        return lang

    def translate(self):
        lang = self.zh_or_en()
        if lang == 'zh':
            data = {
                "query": self.query_str,
                "from": "zh",
                "to": "en",
            }
        else:
            data = {
                "query": self.query_str,
                "from": "en",
                "to": "zh",
            }
        response = requests.post(self.post_url, data=data, headers=self.headers)
        dict_res = json.loads(response.content.decode())
        result = dict_res['trans'][0]['dst']
        print("{}: {}".format(self.query_str, result))


mytranslator = Translator("人生苦短，我用python")
mytranslator.translate()
