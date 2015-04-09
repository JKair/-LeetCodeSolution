class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        dictT = {}
        res = []
        for x in xrange(len(s)-9):
            flag = self.tezhengma(s[x:x+10])
            if dictT.has_key(flag):
                if dictT[flag] == 0:
                    res.append(s[x:x+10])
                    dictT[flag] = 1
            else:
                dictT[flag] = 0
        return res
    def tezhengma(self,s):
        res = 0
        for x in s:
            if x == 'A':
                res = res + 0
            elif x == 'C':
                res = res + 1
            elif x == 'G':
                res = res + 2
            elif x == 'T':
                res = res + 3
            res = res<<3
        return res
