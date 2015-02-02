class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
    	if not A:
    		return 1
        try:
        	token = 1
        	for x in A:
        		if x < 0:
        			continue
        		A.index(token)
        		token = token + 1
        except Exception, e:
        	return token
        return token