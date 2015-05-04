class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
    	res = []
    	for i in xrange(len(s)+1):
    		res.append(False)
    	res[0] = True
    	for x in xrange(len(s)):
    		if res[x]:
    			length = 1
    			while length + x < len(s) + 1:
    				if s[x:x+length] in wordDict:
    					res[x+length] = True
    				length = length + 1
    	return res[len(s)]