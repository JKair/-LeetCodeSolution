Remove Linked List Elements
===========
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5

这道题让我们删除链表里面某个值。

解法：我们创一个token链表，然后当我们遇到不等于val的时候就跳过，如果等于的话，就跳过那个节点就好了。

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
    ListNode* removeElements(ListNode* head, int val) {
        ListNode *temp = new ListNode(-1), *res = temp;
        temp->next = head;

        while (temp->next) {
            if (temp->next->val != val) {
                temp = temp->next;
                continue;
            }

            temp->next = temp->next->next;
        }

        return res->next;
    }
};
```
