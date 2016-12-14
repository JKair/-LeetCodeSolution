Pascal's Triangle
==========
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

让我们生成n阶杨辉三角。

解法：不是太难，最主要注意边界处理就可以了。

```
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        if (numRows == 0) return {};
        vector<vector<int>> res;
        vector<int> temp;
        temp.push_back(1);
        res.push_back(temp);

        for (int i = 1; i < numRows; i++) {
            temp.clear();
            for (int j = 0; j <= i; j++) {
                if (j == i) temp.push_back(res[i - 1][j - 1]);
                else if (j == 0) temp.push_back(res[i - 1][j]);
                else temp.push_back(res[i - 1][j] + res[i - 1][j - 1]);
            }
            res.push_back(temp);
        }

        return res;
    }
};
```
