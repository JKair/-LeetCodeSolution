class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        res = []
        if len(s) == 0 or s == '0':
        	return 0
        for x in xrange(len(s)):
        	res.append(0)
        if s[-1] == '0':
        	res[-1] = 0
        else:
        	res[-1] = 1
        res.append(1)
        x = len(s) - 2
        while x >= 0:
        	if s[x] == '0':
        		x = x - 1
        		continue
        	if s[x] == '1' or (s[x] == '2' and ord(s[x+1]) <= ord('6')):
        		res[x] = res[x+1] + res[x+2]
        	else:
        		res[x] = res[x+1]
        	x = x - 1
        return res[0]