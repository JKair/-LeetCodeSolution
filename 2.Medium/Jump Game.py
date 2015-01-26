class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
    	if len(A) == 0:
    		return False
        i = 0
        step = A[0]
        while True:
        	step = max(step,A[i])
        	step = step - 1
        	i = i + 1
        	if step < 0:
        		break
        	if i>len(A)-1:
        		break
        return i == len(A)