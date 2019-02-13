# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.

from collections import Counter


class Node:
    def __init__(self, char, count, left=None, right=None):
        self.char = char
        self.count = count
        self.left = left
        self.right = right


def huffman_tree(string):
    chars = Counter(string).most_common()
    tree = [Node(char[0], char[1]) for char in chars]
    tree = sorted(tree, key=lambda node: node.count)
    while len(tree) > 1:
        left = tree.pop(0)
        right = tree.pop(0)
        count = left.count + right.count
        index = 0
        while index < len(tree) and count > tree[index].count:
            index += 1
        tree.insert(index, Node(None, count, left, right))
    return tree[0]


def huffman_table(string):
    def _huffman_table(tree, dct, code=''):
        if tree.char is not None:
            dct[tree.char] = code
            return
        if tree.left is not None:
            _huffman_table(tree.left, dct, code + '0')
        if tree.right is not None:
            _huffman_table(tree.right, dct, code + '1')

    tree = huffman_tree(string)
    dct = {}
    _huffman_table(tree, dct)
    return dct


def huffman_pack(string):
    table = huffman_table(string)
    ret = [len(table)]
    for char, code in table.items():
        ret.append(char)
        ret.append(len(code))
        ret += list(code)
    for char in string:
        ret += list(table[char])
    return ret


def huffman_unpack(data):
    ret = ''
    table_len = int(data[0])
    table = {}
    index = 1
    for _ in range(table_len):
        char = data[index]
        code_len = int(data[index + 1])
        code = tuple(data[index + 2: index + 2 + code_len])
        table[code] = char
        index += 2 + code_len
    code = []
    while index < len(data):
        code.append(data[index])
        index += 1
        if tuple(code) in table:
            ret += table[tuple(code)]
            code.clear()
    return ret


packed = huffman_pack(
    'In computer science and information theory, a Huffman code is a particular type of optimal prefix code that is commonly used for lossless data compression.')

print(huffman_unpack(packed))
