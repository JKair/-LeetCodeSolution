class Solution:
    def convert(self, s, nRows):
    	if nRows == 1 or nRows>len(s) :
    		return s
    	resultToken = []
    	for i in range(nRows):
    		resultToken.append("")
    	gmap = nRows-2
    	row = 0
    	result = ""
    	while True:
    		for i in range(nRows):
    			if row == len(s):
    				break
    			resultToken[i] = resultToken[i] + s[row]
    			row = row + 1
    		j = gmap
    		while True:
    			if j == 0 or row == len(s):
    				break
    			resultToken[j] = resultToken[j] + s[row]
    			row = row + 1
    			j = j - 1
    			
    		if row == len(s):
    			break
    	for value in resultToken:
    		result = result + value
    	return result
