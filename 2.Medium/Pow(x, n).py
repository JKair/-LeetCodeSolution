class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        return self.halfPow(x,n)
    def halfPow(self,x,n):
    	result = 1
    	if n<0:
    		n = -n
    		x = 1/x
    	if n == 0:
    		return 1
    	while n != 0:
    		if n&1:
    			result = result * x
    		x = x * x
    		n = n // 2
    	return result