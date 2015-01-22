class Solution:
    # @return an integer
    def reverse(self, x):
    	resultToken = str(x)
    	result = ""
    	if resultToken[0] == "-":
    		result = result + resultToken[0]
    		result = result + resultToken[:0:-1]
    	else:
    		result = resultToken[::-1]

    	if int(result)>2147483647:
    		return 0
    	elif int(result)<-2147483647:
    		return 0
    	return int(result)