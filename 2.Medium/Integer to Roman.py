class Solution:
    dict = {'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}
    RomanNum = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    def intToRoman(self, num):
        s = ""
        for key in self.RomanNum:
            while self.dict[key]<=num:
                s += key
                num -= self.dict[key]
        return s