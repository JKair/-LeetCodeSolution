# To change this template, choose Tools | Templates
# and open the template in the editor.
class Solution:
    def singleNumber(self, A):
        result = 0
        for num in A:
            result = result^num
        return result

if __name__ == "__main__":
    A = Solution()
    print A.singleNumber([1,5,1,9,9,8,7,8,7,6,3,6,3])