String to Integer
==================
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.

这道题让我们把字符串转换成整型，其实也没什么技巧，给一组测试用例吧
```
""
"uierwquioryqoreuiy4574567"
"12345436i"
"ui453"
"4325245jkljkljljlk"
"55555555555555555555555555555"
"-32-451235ghh324"
"-"
"1"
"     +004500"
"+23 4564356"
"      +23"
"   -213"
"   -23 23 23"

```
这些过了，应该就过了。

解法：
```
class Solution {
public:
    int myAtoi(string str) {
        if (str.size() == 0) return 0;
        int res = 0,temp=res, flag = false,jump = false;
        if (str[0] == ' ') {
            return myAtoi(str.substr(1,str.size()-1));
        }
        if (str[0] == '-') {
            flag = true;
            jump = true;
        } else if (str[0] == '+') {
            jump = true;
        }

        for (int i = jump ? 1:0; i < str.size(); i++) {
            if (str[i] >= '0' && str[i] <= '9') {
                temp = res * 10 + str[i] - '0';
                if (res != temp / 10) return flag ? INT_MIN:INT_MAX;
                res = temp;
            } else {
                return flag ? res * -1 : res;
            }
        }

        return flag ? res * -1 : res;
    }
};
```
