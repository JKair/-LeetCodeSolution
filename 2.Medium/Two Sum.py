class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        numToken = sorted(num)
        a = 0
        b = len(numToken)-1
        while True:
            if numToken[a] + numToken[b] > target:
                b = b - 1
            elif numToken[a] + numToken[b] < target:
                a = a + 1
            elif a == b:
                break
            else:
                break
        a = num.index(numToken[a])+1
        for x in xrange(len(num)-1,-1,-1):
            if num[x] == numToken[b]:
                b = x + 1
                break
        if a>b:
            a,b = b,a
        return (a,b)