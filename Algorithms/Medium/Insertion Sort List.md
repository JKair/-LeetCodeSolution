Insertion Sort List
========
Sort a linked list using insertion sort.

这道题让我们用插入法来排序一个列表。

解法：我们按照插入法的思路，找到插入那个点，然后重构一棵树就好了。

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
    ListNode* insertionSortList(ListNode* head) {
        ListNode *res = new ListNode(-1), *temp = res;

        while (head) {
            ListNode *next = head->next;
            temp = res;
            while (temp->next && temp->next->val <= head->val) {
                temp = temp->next;
            }

            head->next = temp->next;
            temp->next = head;
            head = next;
        }

        return res->next;
    }
};
```
