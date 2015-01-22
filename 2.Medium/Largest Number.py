class Solution:
    def largestNumber(self, num):
    	num.sort(lambda a,b:int(str(b)+str(a))-int(str(a)+str(b)))
    	result = ""
    	for x in num:
    		result = result + str(x)
    	if int(result)/10 == 0 and int(result)%10 == 0:
    		result = "0"
        return result