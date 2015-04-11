class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        if len(gas) == 0 or len(cost) == 0 or len(gas) != len(cost):
        	return -1
        total,res,start = 0,0,0
        for x in xrange(len(cost)):
        	total = total + gas[x] - cost[x]
        	if res < 0:
        		start = x
        		res = gas[x] - cost[x]
        	else:
        		res = res + gas[x] - cost[x]
        return -1 if total < 0 else start