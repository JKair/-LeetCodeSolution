Integer to Roman
=====================
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

将整型数变成罗马数，在做这个算法之前，要先弄清楚，罗马数是怎么变换的，详情自己百度或者goggle，这里写一下解法

我们建立一个字典，用来查询罗马字，从高位开始计算循环，直到数字为0，退出为所得。

```
class Solution {
public:
    string intToRoman(int num) {
        int nums[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        string romanNum[] = {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
        string res = "";
        for (int i = 0; i < 13; i++) {
            while (num >= nums[i]) {
                res += romanNum[i];
                num -= nums[i];
            }
        }

        return res;
    }
};
```
