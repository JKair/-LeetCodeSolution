#coding=utf-8
import os

title = """
LeetCodeSolution
=================
有些题目没有，要么是进度还没到，要么就是付费题目没钱买，要么就是还没思路，[我的进度](https://leetcode.com/kair/)。

|id|标题|难度|语言|
|:--:|:--:|:--:|:--:|
"""
body = ""
f = open('readme.txt')
line = f.readline()
#标签
tag = {'M' : 'Medium', 'E':'Easy', 'H':'Hard', 'N':'没钱买', 'D':'Mysql'}
readme = []
#路径
algorithmsPath = './Algorithms/'
databasePath = './Database/'
while line:
    readme.append(line)
    line = f.readline()

f.close()

for alg in readme:
    #生成readme
    alg = alg.replace('\n', '')
    alg = alg.split('@')
    body = body + "|" + alg[0] + "|[" + alg[1] + "](https://leetcode.com/problems/"+alg[1].lower().replace(' ','-')+")|"
    lanType = ''
    if len(alg[2]) == 1 :
        lanType = tag[alg[2]] + '|[C++](' + algorithmsPath + tag[alg[2]] + '/' + alg[1] + ".md)" + "|\n"
    elif len(alg[2]) == 2 and alg[2][1] == 'D':
        lanType = tag[alg[2][0]] + '|[Mysql](' + databasePath + tag[alg[2][0]] + '/' + alg[1] + ".md)" + "|\n"
    else:
        lanType = tag[alg[2][0]] + '|'+ tag[alg[2][1]] +'|\n'
    body = body + lanType
    #创建文件
    if len(alg[2]) == 1 and not os.path.exists(algorithmsPath + tag[alg[2]] + '/' + alg[1] + ".md") :
        os.system('touch "' + algorithmsPath + tag[alg[2]] + '/' + alg[1] + '.md"')
    elif len(alg[2]) == 2 and alg[2][1] == 'D' and not os.path.exists(databasePath + tag[alg[2][0]] + '/' + alg[1] + ".md"):
        os.system('touch "' + databasePath + tag[alg[2][0]] + '/' + alg[1] + '.md"')
#README的文本生成
res = title+body

with open("README.md", 'wb') as code:
    code.write(res)
