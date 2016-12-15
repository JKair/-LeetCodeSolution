Valid Palindrome
=========
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

这道题让我们判断是不是回文，但是这道题需要跳过空格逗号那些特殊字符，而且数字也是处理范围。

解法：这道题由于要我们对大小写进行不敏感处理，所以大小写判断的条件就要格外重要。这里要注意啊，不能直接判断是不是等于小写字母+32！
```
class Solution {
public:
    bool isZimu(char s) {
        if (s >= 'a' && s <= 'z') return true;
        if (s >= 'A' && s <= 'Z') return true;
        if (s >= '0' && s <= '9') return true;
        return false;
    }
    bool isPalindrome(string s) {
        int start = 0, end = s.size() - 1;
        while (start <= end) {
            if (!isZimu(s[start])) start++;
            else if (!isZimu(s[end])) end--;
            else if ((s[start] + 32 - 'a') %32 != (s[end] + 32 - 'a') % 32) {
                return false;
            } else {
                start++;end--;
            }
        }

        return true;
    }
};
```
