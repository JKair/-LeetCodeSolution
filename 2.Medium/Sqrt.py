class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        left = 0
        right = x
        while left <=right:
        	mid = (left + right) / 2
        	if mid*mid > x:
        		right = mid -1
        	else:
        		if (mid+1)*(mid+1) > x:
        			return mid
        		else:
        			left = mid + 1