import random


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


# 逆置换
def generate_inverse_ip_table(ip_table):
    inverse_ip_table = [0] * 64  # 初始化64位的空表
    for i, position in enumerate(ip_table):
        inverse_ip_table[position - 1] = i + 1  # 还原位置
    return inverse_ip_table


INVERSE_IP_TABLE = generate_inverse_ip_table(IP_TABLE)


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
    c = pc_1_key[:28]
    d = pc_1_key[28:]

    for i in range(1):
        temp_r = r  # r的副本，下一个轮次的l = 本轮次r
        if i+1 == 1 or i+1 == 2 or i+1 == 9 or i+1 == 16:
            # 循环左移一位
            c = c[1:] + c[:1]
            d = d[1:] + d[:1]
        else:
            # 循环左移两位
            c = c[2:] + c[:2]
            d = d[2:] + d[:2]
        r = F_function(r, l)
        # li = r(i-1)
        l = temp_r
    return


def F_function(r, l):
    temp = expand_r(r)
    r_48 = ''.join(map(str, temp))
    print(r_48)
    return 0


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


def __main__():
    key = generate_key()
    print("密钥为：", key)
    # 分为8字节一组（64bit）
    print("PC1置换后密钥为：", permuted_choice_1(key))
    data_slides = divide_data("abcdefghijklmnopqrstuvwxyz", 8)
    for data in data_slides:
        binary_data = string_to_binary(data)
        permutation_data = initial_permutation(binary_data)
        encryption(permutation_data, key)


__main__()
