Reverse Nodes in k-Group
======
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: `1->2->3->4->5`

For k = 2, you should return: `2->1->4->3->5`

For k = 3, you should return: `3->2->1->4->5`

这道题让我们逆转链表，每k个就逆转一次。

解法：我们将这道题分解为两部分，一部分就是旋转的部分，一部分则是找到要旋转的链表，这样就比较容易解决问题了。我们用两个参数，一个参数代表了，链表结束的时候，另一个参数则是链表开始的时候，然后每次遍历，当遇到满足的深度，就旋转，拼接，直到整个链表遍历完。

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
    ListNode *reverse(ListNode *pre, ListNode *next) {
        ListNode *last = pre->next;
        ListNode *cur = last->next;
        while(cur != next) {
            last->next = cur->next;
            cur->next = pre->next;
            pre->next = cur;
            cur = last->next;
        }
        return last;
    }

    ListNode* reverseKGroup(ListNode* head, int k) {
        if (!head || k == 1) return head;
        ListNode *temp = new ListNode(-1), *cur = head, *pre = temp;
        temp->next = head;
        int deep = 0;
        while (cur) {
            deep++;
            if (deep % k == 0) {
                pre = reverse(pre, cur->next);
                cur = pre->next;
            } else {
                cur = cur->next;
            }
        }

        return temp->next;
    }
};
```
