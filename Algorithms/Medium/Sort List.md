Sort List
=======
Sort a linked list in O(n log n) time using constant space complexity.

要我们排序一个链表，并且排序算法的时间复杂度不能高于O(nlogn)。

解法：这里使用归并排序解决问题，排序在算法里算是老生常谈了，就不详细解释这个算法了，网上的资料很多。

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
    ListNode* sortList(ListNode* l1, ListNode* l2) {
        if (!l1) return l2;
        if (!l2) return l1;

        if (l1->val < l2->val) {
            l1->next = sortList(l1->next, l2);
            return l1;
        } else {
            l2->next = sortList(l1, l2->next);
            return l2;
        }
    }

    ListNode* sortList(ListNode* head) {
        if (!head || !head->next) return head;
        ListNode *l1 = head, *l2 = head, *temp = head;
        while (l2 && l2->next) {
            temp = l1;
            l1 = l1->next;
            l2 = l2->next->next;
        }
        temp->next = NULL;
        return sortList(sortList(head), sortList(l1));
    }
};
```
