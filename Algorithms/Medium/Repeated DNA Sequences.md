Repeated DNA Sequences
===========
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,
```
Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].
```

这道题计算，连续的10个字符出现次数不止一次的个数。

解法：由于我们已经知道了，要计算的字符是10个，所以，我们可以使用map去解决问题，就是将这个字符串可以形成的子序列切分，然后写进map。
```
class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        if (s.size() < 10) return {};
        vector<string> res;
        map<string, int> flag;

        for (int i = 0; i < s.size() - 9; i++) {
            string temp = s.substr(i, 10);

            if (flag.find(temp) != flag.end()) {
                if (flag[temp] == 0) {
                    res.push_back(temp);
                    flag[temp] = 1;
                }
            } else {
                flag[temp] = 0;
            }
        }

        return res;
    }
};
```
