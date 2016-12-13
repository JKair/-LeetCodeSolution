Implement strStr()
===================
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

这道题让我们找出`needle`，在`haystack`，首次数显的位置，如果不存在则返回-1，`needle = 0` 则返回0。

解法一：我们只需要很直白的，直接遍历，一个字母一个字母比对，如果子字符串有字符匹配不到，就跳出，母字符串移动一位进行下次匹配，这样匹配过去就可以直接ac了。

```
class Solution {
public:
    int strStr(string haystack, string needle) {
        if (needle.empty()) return 0;
        int m = haystack.size(), n = needle.size();
        if (m < n) return -1;

        for (int i = 0; i <= m - n; i++) {
            int j = 0;
            for (; j < n; j++) {
                if (haystack[i+j] != needle[j]) {
                    break;
                }
            }

            if (j == n) return i;
        }

        return -1;
    }
};
```

解法二：实际上，有很多字符串匹配算法，最经典的kmp、bm。但这里我要隆重介绍[sunday](http://m.blog.csdn.net/article/details?id=50767615)，这个算法的实现难度实在比前两个要低得多，而且更好理解，可以进去那个网站里面看，里面说的非常清楚，这里我就不赘述了，贴一下我的实现代码。

```
class Solution {
public:
    int strStr(string haystack, string needle) {
        if (needle.empty()) return 0;
        int next[256] = {0}, n = needle.size(), m = haystack.size();
        for (int i = 0; i < n; i++)
            next[needle[i]] = i;


        for (int i = 0;i <= m - n;) {
            int j = 0, jump = 0;
            for (; j < n; j++) {
                if (needle[j] != haystack[j+i]) break;
            }

            if (j == n) return i;
            else {
                while (next[haystack[i+n+jump]] == 0 && i+n+jump <= m) {
                    jump++;
                }
                if (i+n+jump > m) break;
                i = i + (n - next[haystack[i+n+jump]]) + jump;
            }
        }

        return -1;
    }
};
```
