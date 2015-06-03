class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        if n == 1:
        	return True
        elif n == 0:
        	return False
        res = []
        while True:
        	num = 0
        	while n != 0:
	        	i = n % 10
	        	n = n / 10
	        	num = num + i**2
	        if num == 1:
	        	return True
	        elif num in res:
	        	return False
	        n = num 
	        res.append(num)