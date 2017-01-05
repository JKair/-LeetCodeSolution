Basic Calculator
==========
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
```
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
```

计算器，让我们计算等式的值。

解法：这道题因为不用计算乘除，所以其实难度降低了很多。我们可以用一个容器来记录每次加减的符号，当我们遇到加的时候，直接放进1，减的时候直接放进-1，然后遇到数字的时候，每次都用当前这个数字乘以对容器最后面的数字，即1或者-1，最后还有一层处理是本题的关键，就是括号，当我们遇到左括号的时候，要对左括号前面的符号进行判断，如果是+，那么就直接放进1，如果是-，那么往后的符号都要变成相反。

```
class Solution {
public:
    int calculate(string s) {
        int res = 0;
        vector<int> temp(2, 1);

        for (int i = 0; i < s.size(); i++) {
            if (s[i] >= '0') {
                int num = 0;
                while (i < s.size() && s[i] >= '0') {
                    num = num * 10 + s[i] - '0'; i++;
                }

                res += num * temp.back();
                temp.pop_back();
                i--;
                continue;
            } else if (s[i] == ')') temp.pop_back();
            else if (s[i] != ' ') {
                char now = s[i] == '-' ? -1 : 1;
                temp.push_back(temp.back() * now);
            }
        }

        return res;
    }
};
```
