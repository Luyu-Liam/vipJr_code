# !/usr/bin/python
# coding: utf8
# Time: 2019/4/13 18:39
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
from mylibs.constant import *


def encode(ver, ecl, str):
    mode_encoding = {
        'numeric': numeric_encoding,
        'alphanumeric': alphanumeric_encoding,
        'byte': byte_encoding,
        'kanji': kanji_encoding
    }

    ver, mode = analyse(ver, ecl, str)

    print('line 16: mode:', mode)

    code = mode_indicator[mode] + get_cci(ver, mode, str) + mode_encoding[mode](str)

    # Add a Terminator
    rqbits = 8 * required_bytes[ver - 1][lindex[ecl]]
    b = rqbits - len(code)
    code += '0000' if b >= 4 else '0' * b  # 如果剩余位数大于四位那么填充结束符，否则把剩余的位数全部填0

    # Make the Length a Multiple of 8
    while len(code) % 8 != 0:  # 为了保证数据都是八位一组，如果不足我们在数据后面填入足够位数的0
        code += '0'

    # Add Pad Bytes if the String is Still too Short
    while len(code) < rqbits:
        code += '1110110000010001' if rqbits - len(code) >= 16 else '11101100'

    data_code = [code[i:i + 8] for i in range(len(code)) if i % 8 == 0]
    data_code = [int(i, 2) for i in data_code]

    g = grouping_list[ver - 1][lindex[ecl]]
    data_codewords, i = [], 0
    for n in range(g[0]):
        data_codewords.append(data_code[i:i + g[1]])
        i += g[1]
    for n in range(g[2]):
        data_codewords.append(data_code[i:i + g[3]])
        i += g[3]

    return ver, data_codewords
