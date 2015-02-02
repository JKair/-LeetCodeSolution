class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s): 
        token = s.split(' ')
        result = ""
        for x in xrange(len(token)-1,-1,-1):
        	if token[x]!="":
        		result = result + " " + token[x]
        return result[1:]