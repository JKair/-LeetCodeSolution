Add Two Numbers
==============

You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

这道题给你两个链表，然后让你将两个链表相加起来，题目只需要你考虑个位数加个位数的情。具体做法也很简单，没有特别的技巧，创建一个新的链表，然后相加，处理大于10的情况，最高位需要额外的处理一下，搜了很多解法，基本都差不多，只是代码简洁性各不相同。

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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *res = new ListNode(-1),*temp = res;
        int sum = 0, val1 = 0, val2 = 0, flag = 0;

        while (l1 || l2) {
            val1 = l1 ? l1->val : 0;
            val2 = l2 ? l2->val : 0;
            sum = val1 + val2 + flag;
            flag = sum / 10;
            temp->next = new ListNode(sum % 10);

            temp = temp->next;
            if (l1) l1 = l1->next;
            if (l2) l2 = l2->next;
        }
        if (flag) temp->next = new ListNode(1);

        return res->next;
    }
};
```
