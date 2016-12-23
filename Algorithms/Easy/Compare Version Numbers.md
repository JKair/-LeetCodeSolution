Compare Version Numbers
==================
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37

这个让我们比较版本。

解法：因为版本是一个一个以"."为分隔符来比的，举个例子`1.1.1.1.1.1.1.1.1.1.1.1`版本肯定是小于`2.0`的，所以我们只要比较第一位就好了，同理上面的例子不和`2.0`比，和`1.1.1.1.1.1.2`比，还是后者大，所以我们还是比较前几位就好，并不需要算一个完整的数字出来。

```
class Solution {
public:
    int compareVersion(string version1, string version2) {
        int n1 = version1.size(), n2 = version2.size();
        string s1 = "", s2 = "";
        int i = 0, j = 0;
        while (i < n1 || j < n2) {
            while (i < n1 && version1[i] != '.') {
                s1.push_back(version1[i++]);
            }

            while (j < n2 && version2[j] != '.') {
                s2.push_back(version2[j++]);
            }

            int d1 = atoi(s1.c_str()), d2 = atoi(s2.c_str());

            if (d1 > d2) return 1;
            else if (d1 < d2) return -1;

            s1.clear(); s2.clear();
            i++,j++;
        }

        return 0;
    }
};
```
