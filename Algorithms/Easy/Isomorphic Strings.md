Isomorphic Strings
======
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

这道题让我们判断两个字符串的格式是否一样，就像我们以前学成语一样，`日日夜夜`和`马马虎虎`一样是`AABB`格式的，所以两个的格式是相等的。

解法：我们可以弄一个字典，将对应的字母给对应起来，每次我们查字典就可以知道情况了。这里有一个点，就是我们必须把两个字符串反过来再判断一次，因为会遇到一种状况`abc`对应`aaa`。这样我们的第一次判断就会直接被判断为true，如果你反过来判断就会不成立了，假设两个字符串格式真的是一样的，那么正反判断都是一样的结果。

```
class Solution {
public:
    bool right(string s, string t) {
        map<char, char> flag;

        for (int i = 0; i < s.size(); i++) {
            if (!flag.count(s[i])) {
                flag[s[i]] = t[i];
            }

            if (flag[s[i]] != t[i]) {
                return false;
            }
        }

        return true;
    }
    bool isIsomorphic(string s, string t) {
       if (s.size() != t.size()) return false;
       else if (s == t) return true;

       return right(s, t) && right(t, s);
    }
};
```
