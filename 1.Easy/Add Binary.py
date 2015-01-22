class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
    	a = a[::-1]
    	b = b[::-1]
    	a = self.change(a)
    	b = self.change(b)
        return str(bin(a+b))[2:]
    def change(self,a):
    	token = 0
    	result = 0
    	for x in a:
    		result = result + int(x)*(2**token)
    		token = token + 1
    	return result