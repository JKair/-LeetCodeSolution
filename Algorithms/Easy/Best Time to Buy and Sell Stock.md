Best Time to Buy and Sell Stock
============
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.

这道题就是让我们买股票，从左往右就是第n天的意思，然后让我们算出，最多能够赚多少钱。

解法：这道题其实我们要记录就是今天为止以前最低点的买入是多少，因为能够赚钱的必定是升序的，然后不停地维护最低点和当天价格的差以及最大值之间就可以解决这个问题了。
```
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() == 0) return 0;
        int res = 0, minPrice = prices[0];

        for (int i = 1; i < prices.size(); i++) {
            res = max(prices[i] - minPrice, res);
            minPrice = min(prices[i], minPrice);
        }

        return res;
    }
};
```
