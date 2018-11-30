# 首先需要导入os模块。
# OS取自“operation system”的缩写，意为与操作系统相关的模块。
import os

# 1. 获取当前目录
# print(os.getcwd())

# 2. 创建文件夹
# os.mkdir(os.getcwd() + "/newZone")
# try:
#     os.chdir('D:\LUYU\Algorithm\mydir')
# except OSError:
#     os.mkdir('D:\LUYU\Algorithm\mydir')
#     os.chdir('D:\LUYU\Algorithm\mydir')
# os.chdir('D:\LUYU\Algorithm')
# print(os.getcwd())
# print(os.listdir(os.getcwd()))
# result = os.listdir(os.getcwd())
# for item in result:
#     if os.path.isdir(item):
#         print('是一个文件夹')
#     elif os.path.isfile(item):
#         print('是一个文件')

# print(os.path.split('D:/LUYU/Algorithm/mydir/test.py'))
# dir_path = os.path.split('D:/LUYU/Algorithm/mydir/test.py')
# file_path = dir_path[1].split(".")
# os.rename('D:/LUYU/Algorithm/mydir/test.py', file_path[0] + 'code' + file_path[1])

def renameFile(dirName):
    os.chdir(dirName)
    result = os.listdir(os.getcwd())
    print(result)
    for item in result:
        if os.path.isfile(item):
            raw_path = os.path.join(dirName, item)
            dir_path = os.path.split(raw_path)
            print(dir_path)
            file_path = dir_path[1].split(".")
            print(file_path)
            os.rename(raw_path, "new_" + dir_path[1])
            # os.rename(raw_path, file_path[0] + "new_." + file_path[1])

renameFile("D:\LUYU\Algorithm")

