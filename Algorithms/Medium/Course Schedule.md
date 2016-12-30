Course Schedule
========
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

`2, [[1,0]]`

There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

`2, [[1,0],[0,1]]`

There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

这道题让我们看一下我们能不能修完所有的课程，我们读大学的时候，想修其他门课程的时候，有时候会有一些课有先修课程，而且有可能不止一门，所以有些课不能直接修，有些课没有先修课程，就可以直接修。

解法：这道题是典型的拓扑排序，图论的基础。每门节点有可能有一个或者多个其他节点限制，每次都输出都只能输出入度为0的节点，也就是没有其他节点限制的节点。

1. 我们需要一个数组`flag`来记录那些课程需要先修的课程的门数，也就是每个课程的入度为多少，然后把那些入度为0的课程放进一个入度0容器`zeroIndex`，还需要一个总的所有课程的入度`edags`。
1. 如果这些入度为0的课程，是其他某门课的先修课程，那么对应的`flag`的入度都-1，判断这门课程是否因为修了前面这门课而入度变为0了，如果变为0，那么就可以放进`zeroIndex`了，此时`edags - 1`。
1. 按照2的逻辑如果`zeroIndex`的容器空了，那么最后判断`edags`是否为0，为0说明我们输出了所有的节点，也就是说修完了所有的课程。

```
class Solution {
public:
    bool canFinish(int numCourses, vector<pair<int, int>>& prerequisites) {
        vector<int> zeroIndex, flag(numCourses, 0);
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

            for (int i = 0; i < prerequisites.size(); i++) {
                if (prerequisites[i].second == temp) {
                    flag[prerequisites[i].first]--;
                    if (flag[prerequisites[i].first] == 0) zeroIndex.push_back(prerequisites[i].first);
                    edags--;
                }
            }
        }

        return edags == 0;
    }
};
```
