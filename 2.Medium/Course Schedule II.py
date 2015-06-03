class Solution:
    def dfs(self,u):
        if self.color[u]==2:
            return True 
        if self.color[u]==1:
            return False
        self.color[u]=1
        for v in self.graph[u]:
            if not self.dfs(v):
                return True
        self.order.insert(0,u)
        self.color[u]=2
        return True
    def findOrder(self, numCourses, prerequisites): 
        self.color=[0 for i in range(numCourses)]
        self.graph=[[] for i in range(numCourses)]
        self.order=[]
        for i in range(len(prerequisites)):
            [v,u]=prerequisites[i]
            if not v in self.graph[u]:
                self.graph[u].append(v)
        for i in range(numCourses):
            if not self.dfs(i):
                return [] 
        return self.order 