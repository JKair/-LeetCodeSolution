Merge Two Sorted Lists
====================

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

这道题让我们连接两个有序的链表

由于链表已经有序了，我们可以创建一个新的指针，将两个链表连起来，当l1>l2的时候，那么新的链表下一节点就是l2，否则则相反，最后还要处理，如果其中一个链表还没有结束，那么让新链表的下一节点直接接上那个链表，这样就拼凑完毕了.

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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode *res = new ListNode(-1), *temp = res;

        while (l1 && l2) {
            if (l1->val > l2->val) {
                res->next = l2;
                l2 = l2->next;
            } else {
                res->next = l1;
                l1 = l1->next;
            }
            res = res->next;
        }

        if (l1) {
            res->next = l1;
        }

        if (l2) {
            res->next = l2;
        }

        return temp->next;
    }
};
```
