Sqrt(x)
========
Implement int sqrt(int x).

Compute and return the square root of x.

让我们计算一下算术平方根，但是注意，返回的是整型，所以如果没有解，必须找一个近似值出来。

关于这道题，我们可以使用二分法找出那个值，但是要注意一个点，当输入大数的时候，会超过int的数值范围，所以必须转换成longlong来处理。

```
class Solution {
public:
    int mySqrt(int x) {
        int left = 0, right = x;

        while (left <= right) {
            long long int mid = left + (right - left) / 2;

            if (mid * mid > x) {
                right = mid - 1;
            } else {
                if ( (mid + 1) * (mid + 1) > x) {
                    return mid;
                } else {
                    left = mid + 1;
                }
            }
        }

        return left;
    }
};
```
