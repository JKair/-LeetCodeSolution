Partition List
=============
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.

这道题让我们划分列表，比x大的不动，然后比x小的放左边。

解法一：找到第一个比x大的节点，用这个节点做flag，然后大的放右边，小的放左边。

```
ListNode* partition1(ListNode* head, int x) {
        ListNode *res = new ListNode(-1), *cur = head;
        res->next = head;
        ListNode *temp = res;
        while (temp->next && temp->next->val < x) temp = temp->next;
        cur = temp;
        while (cur->next) {
            if (cur->next->val < x) {
                ListNode *fuck = cur->next;
                cur->next = fuck->next;
                fuck->next = temp->next;
                temp->next = fuck;
                temp = temp->next;
            } else {
                cur = cur->next;
            }
        }

        return res->next;

    }
```

解法二：创建一个新的链表

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
    ListNode* partition(ListNode* head, int x) {
        ListNode *newList = new ListNode(-1);
        ListNode *temp = new ListNode(-1), *flag = newList;
        temp->next = head;
        ListNode *res = temp;
        while (temp->next) {
            if (temp->next->val >= x) {
                ListNode *fuck = temp->next;
                temp->next = fuck->next;
                fuck->next = NULL;
                flag->next = fuck;
                flag = flag->next;
            } else {
                temp = temp->next;
            }

        }
        temp->next = newList->next;

        return res->next;
    }
};
```
