Simplify Path
=============
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

这道题让我们写出最简的路径。

我们这道题我们可以用栈的思想，但是要做一些总结才可以完全写出。

1. ".."的时候，如果栈不为空则删除栈顶
1. "."的时候，不进行任何操作
1. 字母目录则直接push进去
1. 末尾不以"/"为结尾
1. 必须以"/"为空

```
class Solution {
public:
    string simplifyPath(string path) {
        string res="",temp = ".";
        int i = 0, start = 0;
        vector<string> flag;
        while (i < path.size()) {
            if (path[i] == '/') {
                if (temp == "..") {
                    if (!flag.empty()) flag.pop_back();
                } else if (temp != ".") {
                    flag.push_back(temp);
                }
                temp = ".";
                i++;
            } else {
                start = i;
                while (path[i] != '/' && i < path.size()) i++;
                temp = path.substr(start, i - start);
            }
        }

        if (temp == "..") {
            if (!flag.empty()) flag.pop_back();
        } else if (temp != ".") {
            flag.push_back(temp);
        }

        for (int i = 0; i < flag.size(); i++) {
            res += "/" + flag[i];
        }

        return res == "" ? "/":res;
    }
};
```
