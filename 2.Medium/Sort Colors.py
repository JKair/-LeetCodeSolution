class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
    	A.sort()


class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
    	if A == None or len(A) == 1:
    		return
    	hight = len(A)-1
    	low = 0
    	i = 0
    	while True:
    		if A[i] == 2:
    			A[i],A[hight] = A[hight],A[i]
    			hight = hight - 1
    		elif A[i] == 0:
    			A[i],A[low] = A[low],A[i]
    			low = low + 1
    			i = i + 1
    		else:
    			i = i + 1
    		if i > hight:
    			break