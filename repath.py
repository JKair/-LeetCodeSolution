#coding=utf-8
import os
import shutil

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
    nowPath = 'Algorithms/' + alg[1] + '.md'
    movePath = 'Algorithms/' + nandu[alg[2]] + '/' + alg[1] + '.md'
    shutil.move(nowPath, movePath)
