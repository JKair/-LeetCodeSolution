Intersection of Two Linked Lists
=======
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

这道题让我们返回一个两个链表相接的点。

解法：分为三个步骤走。

1. 找到A的长度和B的长度
1. 将其中一方多出来的长度去除
1. 同时往前走，直到遇到相等的节点为止

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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        int lenA = 0,lenB = 0;
        ListNode *ha = headA, *hb = headB;
        while (headA) {
            lenA++;
            headA = headA->next;
        }
        while (headB) {
            lenB++;
            headB = headB->next;
        }
        headA = ha,headB = hb;
        if (lenA > lenB) {
            for (int i = 0; i < lenA-lenB; i++) headA = headA->next;
        } else {
            for (int i = 0; i < lenB-lenA; i++) headB = headB->next;
        }

        while (headA && headB && headA->val != headB->val) {
            headA = headA->next;
            headB = headB->next;
        }

        return headA && headB ? headA : NULL;
    }
};
```
