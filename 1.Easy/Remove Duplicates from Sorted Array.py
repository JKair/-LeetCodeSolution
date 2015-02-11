class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        flag = 0
        for count in xrange(len(A)):
            if A[count] != A[flag]:
                flag = flag + 1
            A[flag] = A[count]
        return flag+1