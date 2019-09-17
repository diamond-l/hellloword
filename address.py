import re
import os
# f = open('exc.txt.txt','r')
# a = input('输入端口号:')
# pattern = (r'[A-Z]')
# regex = re.compile(pattern)
# while True:
#     for i in f:
#         if a == pattern:
def get_address(file):
    '''

    :param file:查找目标
    :return: 查找到的地址
    '''
    port = input('端口:')
    while True:
        data = ''
        for line in file:
            if line == '\n':
                break
            data += line
        obj = re.match(r'\S+',data)#匹配首单词
        if not obj:
            #文件结束
            return 'PORT ERROR'
        if obj.group() == port:
            #匹配到了
            # pattern = r'(\d{1,3}\.\d{1,3}){3}/\d+'
            pattern = r'(\d{1,3}\.){3}\d{1,3}/\d+'
            pattern = r"[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}"
            m = re.search(pattern,data)
            if m:
                return m.group()




if __name__ == '__main__':
    f = open('exc.txt', 'r')
    print(get_address(f))

