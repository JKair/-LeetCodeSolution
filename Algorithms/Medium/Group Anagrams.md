Group Anagrams
================
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]


让我们把拥有相同字母个数的单词都归到一类。

这道题我们可以利用map，将每个字符串都排个序，然后存进map里面，最后再导回容器就可以了。

```
class Solution {
public:
    string sortS(string s){  
        sort(s.begin(), s.end());  
        return s;  
    }
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        sort(strs.begin(), strs.end());
        map<string, vector<string>> res;
        vector<vector<string>> result;

        for (int i = 0; i < strs.size(); i++) {
            res[sortS(strs[i])].push_back(strs[i]);
        }

        for(auto it = res.begin(); it!= res.end(); it++){  
            result.push_back(it->second);  
        }

        return result;
    }
};
```
