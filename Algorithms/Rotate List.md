Rotate List
===========

Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.

这道题让我们将链表的倒数的第k个的位置断开，然后接回前面。

解法：最直接的思路就是找到位置后直接断开，拼接回去前面。然而我们其实可以将链表变成一个环，然后断开该断开的位置就好了，注意要处理k大于链表长度的情况。


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
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head) return NULL;
        ListNode *temp = head;
        int len = 1;
        while (temp->next) {
            temp = temp->next;
            len++;
        }
        temp->next = head;
        k %= len;
        k = len - k;
        while (k--) {
            temp = temp->next;
        }
        head = temp->next;
        temp->next = NULL;

        return head;
    }
};
```
