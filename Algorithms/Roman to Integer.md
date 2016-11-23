Roman to Integer
==================
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

这道题让我们把罗马数转换成整型数

我们有两种办法，一种是从高位到地位走转换，一种是低位从高位走转换，而核心思想是，罗马数字里面有这样的规律

例如，`IV`，因为`V` > `I`，从左到右，先出现较小的罗马数再出现大的罗马数，右边减去左边则为其所代表的数，所以`IV` = `V` - `I` = 4，
基于这个理解，我们可以用两种解法，一种是从左到右遍历，只要遇到下一位比当前位大，那么减去当前位。一种是从右到左位，则遇到当前位比上一位小，那么减去当前位

第一种：
```
class Solution {
public:
    int romanToInt(string s) {
        map<char, int> dict{{'M', 1000}, {'D',500}, {'C',100}, {'L',50}, {'X',10}, {'V',5}, {'I',1}};
        int res = 0;
        for (int i = 0;i < s.size(); i++) {
            if (i == s.size() - 1 || dict[s[i]] >= dict[s[i+1]]) res += dict[s[i]];
            else res -= dict[s[i]];
        }

        return res;
    }
};
```
第二种：
```
class Solution {
public:
    int romanToInt(string s) {
        map<char, int> dict{{'M', 1000}, {'D',500}, {'C',100}, {'L',50}, {'X',10}, {'V',5}, {'I',1}};
        int res = 0;
        for (int i = s.size() - 1;i >= 0; i--) {
            if (i != s.size() - 1 && dict[s[i]] < dict[s[i+1]]) res -= dict[s[i]];
            else res += dict[s[i]];
        }

        return res;
    }
};
```
