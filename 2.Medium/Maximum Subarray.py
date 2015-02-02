class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        maxSub = A[0]
        token = 0
        for i in A:
        	token = token + i
        	maxSub = max(token,maxSub)
        	token = max(0,token)
        return maxSub