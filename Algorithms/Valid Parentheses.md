Valid Parentheses
=====================
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

这道题让我们验证括号出现的合法性。这里我们只要利用栈就可以很直白的解决了，如果是左边括号那么就直接入栈，如果是右边括号，那么就和栈顶相比，如果是匹配成对的话，那么说明完整，这里还要注意，最后匹配完，栈要是空栈，否则则代表左边括号过多，如果遇到右边括号的时候，栈是空栈，那么就说明右边括号过多，都要返回false。

```
class Solution {
public:
    bool isValid(string s) {
        stack<char> res;
        int dict[256];
        dict['('] = ')';
        dict['['] = ']';
        dict['{'] = '}';
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
                res.push(s[i]);
                continue;
            }

            if (res.empty() || s[i] != dict[res.top()]) {
                return false;
            }

            res.pop();
        }

        return res.empty() ? true : false;
    }
};
```
