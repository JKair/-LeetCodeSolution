class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        return self.changeEr(n).count('1')

    def changeEr(self,n):
        result = ''
        while n != 0:
            result = result + str(n % 2)
            n = n/2
        return result[::-1]
