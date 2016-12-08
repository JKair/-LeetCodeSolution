Remove Duplicates from Sorted List II
============
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

这道题让我们，当有数字重复的情况出现则删除节点。

解法一：由于我们可能会遇到空节点的情况，所以我们可以而外创建多一个节点接上head，去处理这个问题。我们需要两个指针，一个快指针去寻找相同节点结束的点在哪里，一个慢则是将寻找的结果接起来。

```
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (!head) return NULL;

        ListNode *res = new ListNode(0);
        res->next = head;
        ListNode *fast = res;
        while (fast->next) {
            ListNode *temp = fast->next;
            while (temp->next && temp->val == temp->next->val) temp = temp->next;
            if (temp == fast->next) fast = fast->next;
            else fast->next = temp->next;

        }

        return res->next;
    }
};
```

解法二：我们还可以利用容器来做到，筛选节点，先push进去，然后判断上个值是否和本次的值一样，如果一样的话，那么就判断容器尾部是否已经插入这个值了，如果插入过那么就pop_back，如果没的话，那么直接push。

```
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (!head) return NULL;

        vector<ListNode*> res;
        int same = head->val;
        res.push_back(head);
        while (head->next) {
            if (head->next->val == same && !res.empty()) {
                if (res.back()->val == same) res.pop_back();
            } else if (head->next->val != same) {
                same = head->next->val;
                res.push_back(head->next);
            }
            head = head->next;
        }

        for (int i = 1; i < res.size(); i++) {
            res[i - 1]->next = res[i];
        }
        if (!res.empty()) {
            res.back()->next = NULL;
        }

        return res.size() == 0 ? NULL : res[0];
    }
};
```
