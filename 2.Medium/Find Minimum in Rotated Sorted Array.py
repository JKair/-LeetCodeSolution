class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        left = 0
        right = len(num)-1
        while left<right:
            if num[left] < num[right]:
                return num[left]
            mid = left + (right - left)/2
            if num[mid] < num[left]:
                right = mid
            else:
                left = mid + 1
        return num[left]