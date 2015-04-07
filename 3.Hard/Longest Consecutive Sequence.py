class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
    	numlen,longest = len(num),0
        setnum,visited = set(num),set()
        if len(num) == 0 or len(num) == 1:
        	return len(num)
        for n in setnum:
        	if n in visited:
        		continue
        	visited.add(n)
        	m,length = n + 1,1
        	while m in setnum:
        		visited.add(m)
        		length,m = length + 1,m + 1
        	m = n - 1
        	while m in setnum:
        		visited.add(m)
        		length,m = length + 1,m - 1
        	longest = max(longest,length)
        return longest