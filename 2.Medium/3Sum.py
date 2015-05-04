class Solution:
    
    def threeSum(self, num):
        if len(num)<3:
            return []
        res = []
        temp = sorted(num)
        for x in xrange(len(num)-2):
            target = temp[0]
            del temp[0]
            ans = self.twoSum(temp,target)
            if res.count(ans) == 0:
                res.extend(ans)
        return res

    def twoSum(self, num, target):
        ans = []
        a = 0
        b = len(num)-1
        while a<b:
            if num[a] + num[b] > -target:
                b = b - 1
            elif num[a] + num[b] < -target:
                a = a + 1
            else:
                ans.append([target,num[a],num[b]])
                b = b - 1
        return ans


a = Solution()
print a.threeSum([0,-1,1])