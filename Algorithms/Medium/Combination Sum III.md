Combination Sum III
=======
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.


Example 1:

Input: k = 3, n = 7

Output:
```
[[1,2,4]]
```
Example 2:

Input: k = 3, n = 9

Output:
```
[[1,2,6], [1,3,5], [2,3,4]]
```

这道题和Combination Sum，Combination Sum II，差不多。但是这次限定在9以内。

解法：还是dfs，和前面两道题差不多。

```
class Solution {
public:
    void combinationSum3(int k, int n, int start, vector<int> &temp, vector<vector<int>> &res, int now) {
        if (temp.size() == k && now == 0) {
            res.push_back(temp);
            return ;
        }

        for (int i = start; i <= 9; i++) {
            temp.push_back(i);
            combinationSum3(k, n, i + 1, temp, res, now - i);
            temp.pop_back();
        }
    }
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> res;
        vector<int> temp;
        combinationSum3(k, n, 1, temp, res, n);
        return res;
    }
};
```

相似题目[Combination Sum](./Combination Sum.md)、[Combination Sum II](./Combination Sum II.md)
