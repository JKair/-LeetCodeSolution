class Solution:
    def rotate(self, nums, k):
        while k > 0 :
        	nums.insert(0,nums.pop())
        	k = k - 1



class Solution:
    def rotate(self, nums, k):
        token = k%len(nums)
        if token < len(nums) and token != 0:
        	numslen = len(nums)
        	nums.extend(nums[0:numslen-token])
        	del nums[0:numslen-token]
