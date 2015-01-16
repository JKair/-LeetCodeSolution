class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 1:
            return strs[0]
        elif len(strs) == 0:
            return ""
        prefixLength = 0
        for i in range(len(strs[0]) if len(strs[0])<len(strs[1]) else len(strs[1])):
            if strs[0][i] != strs[1][i]:
                break
            else:
                prefixLength = i+1
        common = strs[0][:prefixLength]
        for strToken in strs:
            if strToken == "":
                prefixLength = 0
            for s in range(len(strToken) if len(strToken)<len(common) else len(common)):
                if common[s] != strToken[s]:
                    prefixLength = s
                    break
                elif s+1 == len(strToken) if len(strToken)<len(common) else len(common):
                	prefixLength = len(strToken) if len(strToken)<len(common) else len(common)
            common = common[:prefixLength]
        return common