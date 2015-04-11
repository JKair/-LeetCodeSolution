class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
    	if len(num) < 2:
    		return 0
    	maxNum,minNum = max(num),min(num)
        rang = int(math.ceil(float(maxNum-minNum)/(len(num)-1)))
        buckets = {}
        for x in num:
        	temp = int((x-minNum)/rang)
        	if not buckets.has_key(temp):
        		buckets[temp] = [x,x]
        	else:
        		if buckets[temp][0] > x:
        			buckets[temp][0] = x
        		if buckets[temp][1] < x:
        			buckets[temp][1] = x
        res = 0
        pre = buckets.keys()[0]
        for x in buckets:
        	res = max(res,buckets[x][0]-buckets[pre][1])
        	pre = x
        return res