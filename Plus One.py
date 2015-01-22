class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        result = ""
        for x in digits:
        	result = result + str(x)
        value = str(int(result) + 1)
        valueList = []
        for x in value:
        	valueList.append(int(x))
        return valueList
