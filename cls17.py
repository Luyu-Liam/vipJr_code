# !/usr/bin/python
# coding: utf8
# @Author  : Liam
# @Software: PyCharm
import shutil

# 移动
shutil.move("file_1.txt", r"dir\file_1_new.txt")

# 复制(注意：用的是copy2()函数，而不是copy())
shutil.copy2("file_1.txt", r"dir\file_1_new.txt")

# 如何打开一个文件，进行读写操作
# open()函数的第一个参数表示需要打开的文件，第二个参数表示打开方式。
"""六种文件打开方式：
1. 只读 
1.1 r 只能读，光标在文件顶部

2. 可读可写
2.1 r+ 不会创建不存在的文件。如果直接写文件，则从顶部开始写，覆盖之前此
    位置的内容，如果先读后写，则会在文件末尾追加内容
2.2 w+ 如果文件存在则覆盖，不存在则创建
2.3 a+能够任意移动光标进行读，但是如果写的话，光标始终在末尾，从末尾开始
    写入，不存在则创建
3. 只写 
3.1 w 覆盖整个文件，不存在则创建
3.2 a 即追加（非覆盖写）– 所以初始光标位置始终为末尾，不存在则创建
"""
with open('text.txt', 'w+') as f:
    f.write('张无忌到此一游')
    print(f.read())   # 这里能读取到内容吗？

