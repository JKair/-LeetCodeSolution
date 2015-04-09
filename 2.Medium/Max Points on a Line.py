# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        res  = {}
        res[10000000] = 0
        maxnum = 1
        if len(points) == 0:
            return 0
        for i in points:
            res.clear()
            res[10000000] = 0
            same = 1
            for j in points:
                if i == j:
                    continue
                elif i.x == j.x and i.y == j.y:
                    same = same + 1
                else:
                    flag = 10000000 if j.x == i.x else float((j.y - i.y))/(j.x - i.x)
                    res[flag] = res[flag] + 1 if res.has_key(flag) else 1
            for k in res:
                maxnum = max(res[k]+same,maxnum)
        return maxnum