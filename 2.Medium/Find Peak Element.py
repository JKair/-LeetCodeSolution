class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
    	return num.index(sorted(num)[-1])