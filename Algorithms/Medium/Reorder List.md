Reorder List
===========
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.

这道题给我们一个链表，然后让我们把链表重构，变成`L0→Ln→L1→Ln-1→L2→Ln-2→…`

解法：这道题我们分成三个步骤走

1. 找到链表的中点，断开
1. 将第二个链表逆序
1. 重构链表

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
    void reorderList(ListNode* head) {
        if (!head || !head->next || !head->next->next) return;

        ListNode *slow = head, *fast = head;
        while (fast->next && fast->next->next) {
            fast = fast->next->next;
            slow = slow->next;
        }

        ListNode *mid = slow->next, *temp = NULL;
        slow->next = NULL;
        fast = mid;

        while (fast) {
            ListNode *flag = fast->next;
            fast->next = temp;
            temp = fast;
            fast = flag;
        }

        while (head && temp) {
            ListNode *next = head->next;
            head->next = temp;

            temp = temp->next;

            head->next->next = next;
            head = next;
        }

    }
};
```
