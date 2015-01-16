class Solution:
    # @return a string
    def titleToNumber(self, s):
        title = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        s = s[::-1]
        result = 0
        token = 0
        for n in xrange(len(s)):
        	result = result + ((title.index(s[n])+1) * (26 ** token))
        	token = token + 1
    	return result