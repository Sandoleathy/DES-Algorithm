import random

INVERSE_IP_TABLE = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]
IP_TABLE = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]
S1 = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
]

S2 = [
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
    [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
]

S3 = [
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
    [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
    [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
    [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
]

S4 = [
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
]

S5 = [
    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
    [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
]

S6 = [
    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
    [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
    [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
    [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
]

S7 = [
    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
    [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
    [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
    [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
]

S8 = [
    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
    [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
    [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
    [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
]
S_BOXES = [S1,S2,S3,S4,S5,S6,S7,S8]

# 密钥生成部分
def generate_key():
    key = ''
    for i in range(0, 8):
        key += generate_random_binary_key_with_parity(8)
    # print(key)
    # bin_key = int(key, 2)  # 转换为二进制数
    # print(hex(bin_key))
    return key


# 产生符合奇偶校验的密钥
def generate_random_binary_key_with_parity(length):
    # 使用随机选择 0 或 1，生成指定长度的二进制字符串
    if length < 1:
        return 0
    key = ''
    parity_check = 0
    for i in range(length - 1):
        binary_num = random.choice('01')
        if binary_num == '1':
            parity_check += 1
        key += binary_num
    # 奇偶校验位
    if parity_check % 2 == 0:
        key += '1'
    else:
        key += '0'
    return key


# --------------------------------------------------------------------------------
# 切分明文
def divide_data(data, byte):
    groups = [data[i:i + byte] for i in range(0, len(data), byte)]

    # 如果最后一组不足 n 个字符，则用 padding_char 补全
    if len(groups[-1]) < byte:
        groups[-1] = groups[-1].ljust(byte, '0')
    return groups


# --------------------------------------------------------------------------------
# 将明文字符串转换为二进制码
def string_to_binary(s):
    # 将字符串的每个字符转换为对应的二进制表示
    return ''.join(format(ord(char), '08b') for char in s)


# 将二进制码转换回明文字符串
def binary_to_string(binary_str):
    # 每8位一组，将二进制字符串切分
    chars = [binary_str[i:i + 8] for i in range(0, len(binary_str), 8)]

    # 将每组二进制转换为字符
    return ''.join([chr(int(char, 2)) for char in chars])


# --------------------------------------------------------------------------------


# 初始置换
def initial_permutation(binary_text):
    # 创建一个空的列表，用来存储置换后的位
    permuted_bits = []

    # 遍历初始置换表中的每个元素
    for i in IP_TABLE:
        # 根据置换表的值找到明文中对应的位，并加入置换后的列表
        permuted_bits.append(binary_text[i - 1])

    # 将列表中的位连接成一个新的字符串
    permuted_text = ''.join(permuted_bits)

    # print("置换后的明文:", permuted_text)
    return permuted_text


# 执行逆初始置换的函数
def inverse_permutation(permuted_text):
    return ''.join(permuted_text[i - 1] for i in INVERSE_IP_TABLE)


# --------------------------------------------------------------------------------

# 16轮次加密
def encryption(text, key):
    # 分成两组，每组32bit
    group = divide_data(text, 32)
    # 初始情况下直接分为左右两组
    l = group[0]
    r = group[1]
    # 对密钥进行pc-1替换
    pc_1_key = permuted_choice_1(key)
    # 切分成28bit一部分
    c = pc_1_key[:28]
    d = pc_1_key[28:]

    # 16轮迭代
    for i in range(16):
        temp_r = r  # r的副本，下一个轮次的l = 本轮次r
        # 每轮子密钥k生成
        if i + 1 == 1 or i + 1 == 2 or i + 1 == 9 or i + 1 == 16:
            # 循环左移一位
            c = c[1:] + c[:1]
            d = d[1:] + d[:1]
            # print("循环左移一位，结果为c: ", c, ' ,d: ', d)
        else:
            # 循环左移两位
            c = c[2:] + c[:2]
            d = d[2:] + d[:2]
            # print("循环左移两位，结果为c: ", c, ' ,d: ', d)
        child_key = permuted_choice_2(c, d)
        F_function(r, child_key)
        # r = F_function(r, l)
        # li = r(i-1)
        # l = temp_r
    print("16轮迭代结束")
    return


# F函数
# 接收48位的子密钥和32位的R
def F_function(r, k):
    temp = expand_r(r)
    r_48 = ''.join(map(str, temp))
    # print(len(k), " ", len(r_48))
    xor_list = []
    # 进行异或操作
    for i in range(48):
        if r_48[i] == k[i]:
            xor_list.append('0')
        else:
            xor_list.append('1')
    xor_result = ''.join(xor_list)
    # print(xor_result)
    # 使用异或结果进行S盒替换
    s_box_result = S_box_substitution(xor_result)
    return xor_result


# S盒替换
def S_box_substitution(xor_result):
    # 切分成8个部分，每个部分6bit
    s_box_text = []
    for i in range(8):
        s_box_text.append(xor_result[i*6:(i+1)*6])
    s_num = 0
    s_box_result = ''
    for i in s_box_text:
        # 选择对应的S盒
        s_table = S_BOXES[s_num]
        # 分组的第一位和最后一位组合成行数
        row_binary = i[0] + i[5]
        # 分组的中间四位组成列数
        column_binary = i[1:5]
        # 转化为十进制
        row = int(row_binary, 2)
        column = int(column_binary, 2)
        # 选择S盒中的值
        decimal_result = s_table[row][column]
        # 转换为二进制
        binary_result = bin(decimal_result)
        binary_result = binary_result[2:]   # 去掉0b开头
        # 如果二进制格式不足4位，则在高位补0
        while len(binary_result) < 4:
            binary_result = '0' + binary_result
        # print(binary_result)
        s_box_result += binary_result
        s_num += 1
    return s_box_result


# r扩展到48位，用于执行Feistel函数
def expand_r(r):
    expansion_table = [
        32, 1, 2, 3, 4, 5,
        4, 5, 6, 7, 8, 9,
        8, 9, 10, 11, 12, 13,
        12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21,
        20, 21, 22, 23, 24, 25,
        24, 25, 26, 27, 28, 29,
        28, 29, 30, 31, 32, 1
    ]
    output_48 = [0] * 48
    for i in range(0, 48):
        output_48[i] = r[expansion_table[i] - 1]
    return output_48


# PC-1置换
# 返回的是56bit数据，删除了每字节最后一位奇偶校验位
def permuted_choice_1(key):
    if len(key) != 64:
        return
    permuted_table = [
        57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4
    ]
    pc_1_list = []
    for i in permuted_table:
        pc_1_list.append(key[i - 1])
    pc_1_key = ''.join(pc_1_list)
    return pc_1_key


# PC-2置换
# 返回的48bit数据
def permuted_choice_2(c, d):
    child_key = c + d
    pc2_table = [
        14, 17, 11, 24, 1, 5,
        3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8,
        16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32
    ]
    pc_2_list = []
    for i in pc2_table:
        pc_2_list.append(child_key[i - 1])
    pc_2_key = ''.join(pc_2_list)
    return pc_2_key


def __main__():
    key = generate_key()
    print("密钥为：", key)
    # 分为8字节一组（64bit）
    # print("PC1置换后密钥为：", permuted_choice_1(key))
    data_slides = divide_data("abcdefghijklmnopqrstuvwxyz", 8)
    for data in data_slides:
        binary_data = string_to_binary(data)
        permutation_data = initial_permutation(binary_data)
        encryption(permutation_data, key)


__main__()
