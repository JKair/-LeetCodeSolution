class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
    	result = ""
    	for index in xrange(len(s)):
    		if s[index].isalpha() or s[index].isdigit():
    			result = result + s[index].lower()
        return result[::-1] == result