class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        sin,dou = 0,0
        for x in xrange(len(num)):
        	if x%2 == 0:
        		dou = max (dou + num[x],sin)
        	else:
        		sin = max (sin + num[x],dou)
        return max(dou,sin)