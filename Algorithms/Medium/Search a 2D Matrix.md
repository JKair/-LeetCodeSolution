Search a 2D Matrix
=========
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.

这道题让我们在一个有序的矩阵里面找某个值。

解法一：实际上就是把一维查找变成二维查找了，关于查找，我们可以直接用二分法，这里我们只需要用两次二分法就可以查找到那个值了

```
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.empty() || matrix[0].empty()) return false;
        if (target < matrix[0][0] || target > matrix.back().back()) return false;
        int left = 0, right = matrix.size()-1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (matrix[mid][0] == target) return true;
            else if (matrix[mid][0] > target) right = mid - 1;
            else left = mid + 1;
        }
        int temp = right;
        left = 0, right = matrix[0].size()-1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (matrix[temp][mid] == target) return true;
            else if (matrix[temp][mid] > target) right = mid - 1;
            else left = mid + 1;
        }

        return false;
    }
};
```

解法二：其实也可以使用一次二分法就找出来，可以把整个矩阵看成一行，难点在于坐标的转换，mid代表的是第mid个，那么我们只要对n(一行的个数)取余，就可以知道是在这一行是第几个，然后直接除以n则可以直接得到第几列。

```
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.empty() || matrix[0].empty()) return false;
        if (target < matrix[0][0] || target > matrix.back().back()) return false;
        int left = 0, n = matrix[0].size(), m = matrix.size(), right = m * n -1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (matrix[mid / n][mid % n] == target) return true;
            else if (matrix[mid / n][mid % n] > target) right = mid - 1;
            else left = mid + 1;
        }

        return false;
    }
};
```
