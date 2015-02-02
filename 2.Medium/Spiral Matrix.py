# coding: UTF-8
class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
    	if not matrix:
    		return matrix
        top,bot,left,right = 0,len(matrix)-1,0,len(matrix[0])-1
        result = []
        while top<=bot or left<=right:
        	#头
        	result = result + matrix[top][left:right+1]
        	top = top + 1
        	if top>bot:
        		break
        	#右
        	token = top
        	while token <= bot:
        		result.append(matrix[token][right])
        		token = token + 1
        	right = right - 1
        	if left>right:
        		break
        	#下
        	result = result + [matrix[bot][i] for i in xrange(right,left-1,-1)]
        	bot = bot - 1
        	if bot < top:
        		break
        	#左
        	token = bot
        	while token >= top:
        		result.append(matrix[token][left])
        		token = token -1
        	left = left + 1
        	if left>right:
                    break
        return result