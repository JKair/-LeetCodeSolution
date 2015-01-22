class Solution:
    dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    def romanToInt(self, s):
        result = 0
        i = len(s)-1        
        result += self.dict[s[i]]
        i -= 1
        while i>=0:
            if self.dict[s[i+1]]>self.dict[s[i]]:
                result -= self.dict[s[i]]
                i-=1
            else :
                result += self.dict[s[i]]
                i-=1
        return result

