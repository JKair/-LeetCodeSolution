class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        #return haystack.find(needle)  最简单的方法，一行搞定
        return self.sunday(haystack,needle)     #这里使用的是sunday算法

    def sunday(self,haystack,needle):
        hindex = 0
        if len(haystack)<len(needle):
            return -1
        elif len(haystack) == len(needle) and haystack=="":
            return 0
        elif len(needle) == 0:
            return 0
        while hindex < len(haystack):
            if self.find(haystack,needle,hindex):
                return hindex
            else:
                hindex = hindex + len(needle)
                if hindex >= len (haystack):
                    return -1
                for index  in xrange(len(needle)-1,-1,-1):
                    if haystack[hindex] == needle[index]:
                        hindex = hindex - index
                        break
                if len(haystack) + hindex + 1 < len(needle):
                    return -1
        return -1

    def find(self,haystack,needle,hindex):
    	i = 0
    	com = 0
    	for index in xrange(hindex,len(haystack)):
    		if haystack[index] == needle[i]:
    			com = com + 1
    		else:
    			return False
    		if com == len(needle):
    			return True
    		i = i + 1