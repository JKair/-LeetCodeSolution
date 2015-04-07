class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        num = self.changeEr(n)
        if len(num) != 32:
            for x in xrange(32 - len(num)):
                num = num + '0'
        return self.changeShi(num)


    def changeEr(self,n):
    	result = ''
    	while n != 0:
    		result = result + str(n % 2)
    		n = n/2
    	return result

    def changeShi(self,n):
        i = 0
        result = 0
        n = n[::-1]
        for x in xrange(len(n)):
            result = result + int(n[x])*2**i
            i = i + 1
        return result