class Solution:
    # @return an integer
    def atoi(self, str):
    	if str=="":
    		return 0
    	str = str.lstrip()
    	nowS = ""
    	for index in range(len(str)):
    		if str[index] == " " or str[index].isalpha():
    			break
    		if str[index]=="+" or str[index] == "-":
    			if str[index+1]=="+" or str[index+1]=="-":
    				break
    		nowS = nowS + str[index]
    	flag = True
    	if len(nowS)==1 and not nowS.isdigit() or nowS=="":
    		flag = False

    	if not flag:
    		return 0
    	else:
    		if int(nowS)>2147483647:
    			return 2147483647
    		elif int(nowS)<-2147483648:
    			return -2147483648
    		else:
    			return int(nowS)