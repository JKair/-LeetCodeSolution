class Solution(object):
    def moveZeroes(self, nums):
    	flag_zero = 0 if nums[0] == 0 else None
    	for i in xrange(len(nums)):
    		if nums[i] == 0:
    			if flag_zero == None:
    				flag_zero = i
    			else:
    				flag_zero = i if flag_zero > i else flag_zero
    		elif nums[i] != 0 and flag_zero != None:
    			nums[flag_zero] = nums[i]
    			nums[i] = 0
    			flag_zero = i if nums[flag_zero + 1] != 0 else flag_zero + 1
a = Solution()
print a.moveZeroes([1,0,1])