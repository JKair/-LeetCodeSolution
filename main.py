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
nandu = {'M' : 'Medium', 'E':'Easy', 'H':'Hard', 'N':'没钱买'}
readme = []
algorithmsPath = './Algorithms/'
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
        lanType = nandu[alg[2]] + '|[C++](' + algorithmsPath + nandu[alg[2]] + '/' + alg[1] + ".md)" + "|\n"
    else:
        lanType = nandu[alg[2][0]] + '|'+ nandu[alg[2][1]] +'|\n'
    body = body + lanType
    #创建文件
    if len(alg[2]) == 1 and not os.path.exists(algorithmsPath + nandu[alg[2]] + '/' + alg[1] + ".md") :
        os.system('touch "' + algorithmsPath + nandu[alg[2]] + '/' + alg[1] + '.md"')
res = title+body

with open("README.md", 'wb') as code:
    code.write(res)
