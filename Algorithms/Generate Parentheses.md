Generate Parentheses
===================

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

这道题让我们列出n个括号的所有排列的可能性。

我们可以利用递归来进行罗列，用left和right分别表示左括号和右括号剩下的应该罗列的个数，当left>0的时候，继续罗列左边括号，当right>0的时候，继续罗列右边括号。如果left>right，那么说明当前这种情况是不符合要求的，应该右边的括号插入多余左括号的插入。当left和right同时等于0的时候，则将当前的元素放进容器。具体代码如下：

```
class Solution {
public:
    void generateParenthesis(int left,int right,string temp,vector<string> &res) {
        if (left > right) return;
        if (left == 0 &&  right == 0) {
            res.push_back(temp);
            return;
        }

        if (left > 0) generateParenthesis(left - 1, right, temp + '(', res);
        if (right > 0) generateParenthesis(left, right-1, temp + ')', res);
    }

    vector<string> generateParenthesis(int n) {
        int left = n,right = n;
        vector<string> res;
        string temp="";
        generateParenthesis(left,right,temp,res);

        return res;
    }
};
```
