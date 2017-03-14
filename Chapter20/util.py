# coding=utf-8
def lines(file):
    for line in file: yield line
    yield '\n'  # 最后增加一个换行，防止下面的块函数，不返回最后一个块

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip(): #如果 去掉空格换行符后，也不是空行
            block.append(line)  # 加入行 （不去掉换行符）
        elif block:  # 如果 是空行，而且block不为空
            yield ''.join(block).strip() # 返回块
            block = []  # 清空块