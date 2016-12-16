Gas Station
==========
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.

这道题就是给我们两个数组，一个是加油站能加油的数，另外一个则是过一个站要花费的油，问我们从随机一个点出发，能不能绕一环。

解法：首先我们必须明确一点，就是要能绕一环的前提就是结果加油站加的油的总和必大于或等于消耗的油，因为如果消耗的油大于加油站的油的话，那么必定会在某一环就不能跑了。所以反过来我们可以知道，如果加油站加的油大于消耗的油那么必定有解，接下来我们就要算在哪里有解了。由于本题目并不关心有多解的情况，所以难度有所降低。我们只要有一个变量计算汽车从开始的点到我们遍历到的点是不是可以跑通就行了，如果不能跑通，说明这个起点不对，这时候再将起点换到失败的后面的那个点然后从新跑，如此循环，只要我们发现一个点可以跑到结尾，并且总加油量大于耗油量，那么则该起点便是解。

```
class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        if (gas.empty() || cost.empty() || cost.size() != gas.size()) return -1;

        int res = 0, start = 0, total = 0;

        for (int i = 0; i < gas.size(); i++) {
            total += gas[i] - cost[i];

            if (res < 0) {
                start = i;
                res = gas[i] - cost[i];
            } else {
                res += gas[i] - cost[i];
            }
        }

        return total < 0 ? -1 : start;
    }
};
```
