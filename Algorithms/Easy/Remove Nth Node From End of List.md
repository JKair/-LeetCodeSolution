Remove Nth Node From End of List
================================

Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.


这道题让我们删除结尾往前数n的节点。

第一种解法，先遍历一次链表的长度，然后回来删除。

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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *res = new ListNode(-1), *temp = res, *delList = res;
        res->next = head;
        int deep = 1, del = 0;
        while (temp->next) {
            deep++;
            temp = temp->next;
        }

        del = deep - n - 1;
        while (del--) {
            delList = delList->next;
        }
        delList->next = delList->next->next;

        return res->next;
    }
};
```

但是这种解法不符合题目要求，题目要求我们一次循环搞定它，那么怎么才能一次搞定呢？我们可以利用快慢指针，一个指针跑在前面就好了。

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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *res = new ListNode(-1), *temp = res, *delList = res;
        res->next = head;
        while (n--) {
            temp=temp->next;
        }

        while (temp->next) {
            temp = temp->next;
            delList = delList->next;
        }

        delList->next = delList->next->next;

        return res->next;
    }
};
```
