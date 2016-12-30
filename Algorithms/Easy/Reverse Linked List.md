Reverse Linked List
=======
Reverse a singly linked list.

这道题让我们旋转整个链表。

解法：我们可以通过递归，来将链表拆分到最后一个节点的调换，然后回溯就解决了。

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
    ListNode* reverseList(ListNode* head) {
        if (head == NULL) return NULL;
        else if(head->next == NULL) return head;

        ListNode *n = head->next;
        ListNode *p = reverseList(n);

        head->next = NULL;
        n->next = head;

        return p;
    }
};
```
