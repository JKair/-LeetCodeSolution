#coding=utf-8
import os

title = """
LeetCodeSolution
=================
[算法](https://leetcode.com/problemset/algorithms/)。

|id|标题|难度|语言|
|:--:|:--:|:--:|:--:|
"""
body = ""
f = open('readme.txt')
line = f.readline()
nandu = {'M' : 'Medium', 'E':'Easy', 'H':'Hard'}
readme = []
while line:
    readme.append(line)
    line = f.readline()

f.close()

for alg in readme:
    alg = alg.replace('\n', '')
    alg = alg.split('@')
    body = body + "|" + alg[0] + "|[" + alg[1] + "](https://leetcode.com/problems/"+alg[1].lower().replace(' ','-')+")|" + nandu[alg[2]] + '|[C++](./Algorithms/' + nandu[alg[2]] + '/' + alg[1] +".md)" + "|\n"
res = title+body

with open("README.md", 'wb') as code:
    code.write(res)
