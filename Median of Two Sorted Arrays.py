class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        a = sorted(A+B)
        if len(a)%2 == 0 :
        	return ( a[len(a)/2] + a[len(a)/2 - 1] ) / 2.0
        else:
			return a[len(a)/2]