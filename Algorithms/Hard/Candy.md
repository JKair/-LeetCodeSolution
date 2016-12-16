Candy
====
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

给n个小孩的身高，然后让我们给小孩糖果，只要身高比前面高的小孩，那么得到的糖果则不能少于前面的孩子，问最少需要给多少糖果。

解法：这道题其实把他看做递增数列和递减数列的处理
1. 如果我们发现递增数咧的话，我们只要一次给比前面多一个就可以了。
1. 当我们遇到递减数列的第一个数字的时候，那么要我们就只需要给当前这个小孩一颗就行了，然后往下走，如果还是递减，那么就给前面那个人一颗，也给这个人一颗。
1. 当递减数列开始的第一个人糖果要多于递增数列的最后一个的时候，我们也需要给那个人多一个糖果。


```
class Solution {
public:
    int candy(vector<int>& ratings) {
        int decline = 0, beforeCandy = 1,afterCandy = 1,temp = 1, res=1;

        for (int i = 1; i < ratings.size(); i++) {
            if (ratings[i] >= ratings[i - 1]) {  //处理递增数列
                if (ratings[i] > ratings[i - 1]) {  //如果是递增数列的话，那么维护递增糖果
                    afterCandy++;
                } else {  //如果发现前后身高一样，那么当前这个身高直接给一个糖果就好了
                    afterCandy = 1;
                }
                res += afterCandy;
                beforeCandy = afterCandy;
                decline = 0;
            } else {  //处理递减数列
                decline++;
                if (beforeCandy <= decline) {  //这里要处理的是，如果递减数列，已经走到目前的小朋友糖果数量为0了，那么递增数列的最后一个人也应该给他一个糖果
                    res++;
                }
                res += decline;
                afterCandy = 1;
            }
        }

        return res;
    }
};
```
