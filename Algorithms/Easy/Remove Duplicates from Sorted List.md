Remove Duplicates from Sorted List
==================================
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

这道题让我们删除一个链表上重复的节点

我们只要一个循环，当遇到当前节点和接下来那个节点的值相同的时候，那么就直接跳过下个节点，接上下下个节点。否则就直接遍历下个节点。

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
        ListNode *temp = head;

        while (temp && temp->next) {
            if (temp->next->val == temp->val) {
                temp->next = temp->next->next;
            } else {
                temp = temp->next;
            }
        }

        return head;
    }
};
```

相似题目[Remove Duplicates from Sorted List II](./Remove Duplicates from Sorted List II.md)
