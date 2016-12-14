Best Time to Buy and Sell Stock II
============
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

这道题和之前的`Best Time to Buy and Sell Stock`一样，是要我们卖股票，但是这一次不限次数了，我们可以自由买卖次数。

解法：这道题我感觉其实要比`Best Time to Buy and Sell Stock`简单，因为这里不限次数了，所以其实我们只要前后两天有赚就加起来就好了。

```
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int res = 0, temp = 0;

        for (int i = 1; i < prices.size(); i++) {
            temp = prices[i] - prices[i - 1];
            res += temp > 0 ? temp : 0;
        }

        return res;
    }
};
```
