Linked List Cycle
===========
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

这道题让我们判断是否是环，并且不可以用额外的空间。

解法：关于环的，我们其实使用快慢指针就能很好的解决了，因为假设这个链表是环的话，那么一个跑得快一个跑得慢，那么迟早有一天，那个慢的会被快的追上多一圈。

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
    bool hasCycle(ListNode *head) {
        if (!head) return false;
        ListNode *temp = head;
        while (head && temp && temp->next) {
            temp = temp->next->next;
            head = head->next;
            if (temp == head) return true;
        }

        return false;
    }
};
```
