class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        if len(A)==1:
            return A[0]
        A = sorted(A)
        i = 0
        while i<len(A):
            if A[i]==A[i+1]==A[i+2]:
                i += 3
            else:
                return A[i]^A[i+1]^A[i+2]
            if (i==len(A)-1):
                return A[i]
