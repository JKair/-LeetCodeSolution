Course Schedule II
======
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

For example:

`2, [[1,0]]`

There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]

`4, [[1,0],[2,0],[3,1],[3,2]]`

There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].

这道题和`Course Schedule`是差不多的，不同的地方在于，它要我们输出修的顺序。

解法：实际上就是拓扑排序的一环，我们可以稍微修改一下`Course Schedule`的代码就达到目的了。

```
class Solution {
public:
    vector<int> findOrder(int numCourses, vector<pair<int, int>>& prerequisites) {
        vector<int> zeroIndex, flag(numCourses, 0), res;
        int edags = 0;

        for (int i = 0; i < prerequisites.size(); i++) {
            flag[prerequisites[i].first] += 1;
            edags++;
        }

        for (int i = 0; i < numCourses; i++) {
            if (flag[i] == 0) zeroIndex.push_back(i);
        }

        while (!zeroIndex.empty()) {
            int temp = zeroIndex.back();
            zeroIndex.pop_back();
            res.push_back(temp);
            for (int i = 0; i < prerequisites.size(); i++) {
                if (prerequisites[i].second == temp) {
                    flag[prerequisites[i].first]--;
                    if (flag[prerequisites[i].first] == 0) zeroIndex.push_back(prerequisites[i].first);
                    edags--;
                }
            }
        }

        if (edags != 0) return {};
        else return res;
    }
};
```

相似题目[Course Schedule](./Course Schedule.md)
