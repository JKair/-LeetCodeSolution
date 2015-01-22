class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
    	if len(A) == 0:
    		return len(A)
    	try:
    		while True:
    			del A[A.index(elem)]
    	except Exception, e:
    		return len(A)