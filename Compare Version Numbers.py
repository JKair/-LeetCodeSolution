class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
    	version1Token = version1.split('.')
    	version2Token = version2.split('.')
    	versionSw = 10**(len(version1Token) if len(version1Token)>len(version2Token) else len(version2Token))
    	version1Sum = 0
    	version2Sum = 0
    	for index in range(len(version1Token)):
    		version1Sum = version1Sum + int(version1Token[index]) * versionSw
    		versionSw = versionSw / 10
    	versionSw = 10**(len(version1Token) if len(version1Token)>len(version2Token) else len(version2Token))
    	for index in range(len(version2Token)):
    		version2Sum = version2Sum + int(version2Token[index]) * versionSw
    		versionSw = versionSw / 10
    	if version1Sum>version2Sum:
    		return 1
    	elif version1Sum<version2Sum:
    		return -1
    	else:
    		return 0