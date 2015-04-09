class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        total,length = 0,0
        beforeCandy,afterCandy = 1,1
        if len(ratings) == 1:
        	return 1
        for x in xrange(len(ratings)):
        	if total == 0:
        		total = 1
        	else:
        		if ratings[x] < ratings[x-1]:
        			length = length + 1
        			if beforeCandy <= length:
        				total = total + 1 			#当我发给这个小朋友的糖果已经为0的时候，那我最开始递减的那个人应该多给一个糖果
        			total = total + length			#然后这个递减长度的每个小朋友都要多给一个，所以总共要给lenth+1个
        			afterCandy = 1 					#这个是为了保证每次递减数列完的时候，最后一个人一定只有一个糖果
        		else:
        			if ratings[x-1] < ratings[x]:
        				afterCandy = afterCandy + 1
        			else:
        				afterCandy = 1
        			total = total + afterCandy
        			beforeCandy = afterCandy
        			length = 0
        return total