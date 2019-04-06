# !/usr/bin/python
# coding: utf8
# Time: 2019/4/6 17:47
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
from mylibs.constant import char_cap, required_bytes, mindex, lindex, num_list, alphanum_list, grouping_list, mode_indicator


def numeric_encoding(string):
    # str_list = []
    # for i in range(0, len(str), 3):
    #     str_list.append(str[i:i+3])
    str_list = [string[i:i + 3] for i in range(0, len(string), 3)]
    code = ""
    for i in str_list:
        rqbin_len = 10
        if len(i) == 1:
            rqbin_len = 4
        elif len(i) == 2:
            rqbin_len = 7
        code_temp = bin(int(i))[2:]
        code += ('0' * (rqbin_len - len(code_temp)) + code_temp)
    return code


def alphanumeric_encoding(string):
    code_list = [alphanum_list.index(i) for i in string]
    code = ""
    for i in range(1, len(code_list), 2):
        c = bin(code_list[i - 1] * 45 + code_list[i])[2:]
        code += ('0' * (11 - len(c)) + c)
    if i != len(code_list) - 1:
        c = bin(code_list[-1])[2:]
        code += ('0' * (6 - len(c)) + c)
    return code


def byte_encoding(string):
    code = ""
    for i in string:
        c = bin(ord(i.encode('iso-8859-1')))[2:]
        code += ('0' * (8 - len(c)) + c)
    return code


def kanji_encoding(string):
    pass


def get_cci(ver, mode, string):
    mindex = {'numeric': 0, 'alphanumeric': 1, 'byte': 2, 'kanji': 3}
    if 1 <= ver <= 9:
        cci_len = (10, 9, 8, 8)[mindex[mode]]
    elif 10 <= ver <= 26:
        cci_len = (12, 11, 16, 10)[mindex[mode]]
    else:
        cci_len = (14, 13, 16, 12)[mindex[mode]]

    cci = bin(len(string))[2:]
    cci = '0' * (cci_len - len(cci)) + cci
    return cci


mode_indicator = {
    'numeric': '0001',
    'alphanumeric': '0010',
    'byte': '0100',
    'kanji': '1000'
}

mode_encoding = {
    'numeric': numeric_encoding,
    'alphanumeric': alphanumeric_encoding,
    'byte': byte_encoding,
    'kanji': kanji_encoding
}


def analyse(ver, ecl, string):
    if all(i in num_list for i in string):
        mode = 'numeric'
    elif all(i in alphanum_list for i in string):
        mode = 'alphanumeric'
    else:
        mode = 'byte'

    m = mindex[mode]
    l = len(string)
    for i in range(40):
        if char_cap[ecl][i][m] > l:
            ver = i + 1 if i + 1 > ver else ver
            break
    return ver, mode


def encode(ver, ecl, string):
    ver, mode = analyse(ver, ecl, string)
    print('mode:', mode)
    code = mode_indicator[mode] + get_cci(ver, mode, string) + mode_encoding[mode](string)
    print(code)


if __name__ == '__main__':
    string = '34242'
    encode(1, 'L', string)
