class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
    	if not prerequisites:
    		return True
        indegrees = []
        edges = 0
        zeroIndeg = []
        for i in xrange(numCourses):
        	indegrees.append(0)
        for num in prerequisites:
        	indegrees[num[0]] = indegrees[num[0]] + 1
        	edges = edges + 1
        for i in xrange(len(indegrees)):
        	if indegrees[i] == 0:
        		zeroIndeg.append(i)
        while len(zeroIndeg) != 0:
        	view = zeroIndeg.pop()
        	for i in prerequisites:
        		if i[1] == view:
        			edges = edges - 1
        			indegrees[i[0]] = indegrees[i[0]] - 1
        			if indegrees[i[0]] == 0:
        				zeroIndeg.append(i[0])
        if edges == 0:
        	return True
        else:
        	return False