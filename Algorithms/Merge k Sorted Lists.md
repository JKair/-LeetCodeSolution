Merge k Sorted Lists
====================
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

合并多个排序好的链表。

这道题和之前的[Merge Two Sorted Lists](./Merge Two Sorted Lists.md)差不多。不同的是这次链表不是两个了，变多了，但实际上思路是一样的，就算多个链表，我们也可以两个两个合并。但是这道题要稍微修改一样，减少循环的次数，如果我们每次合并，都用上次合并完的链表和本次要进行合并的链表进行合并，那么合并的次数每次都会是比合并完链表短的那个链表的长度，但是，如果我们每次合并都是没合并过的链表来合并的话，那么合并的次数将会减少很多。

```
class Solution {
public:
    void mergeTwoLists(ListNode* l1, ListNode* l2, vector<ListNode*> &fuck) {
        ListNode *res = new ListNode(0), *temp = res;
        while (l1 && l2) {
            if (l1->val > l2->val) {
                res->next = l2;
                l2 = l2->next;
            } else {
                res->next = l1;
                l1 = l1->next;
            }
            res = res->next;
        }
        if (l1) {
            res->next = l1;
        }
        if (l2) {
            res->next = l2;
        }
        fuck.insert(fuck.begin(),temp->next); // 42ms
        //fuck.push_back(temp->next); 365ms
    }

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.empty()) return NULL;

        while (true) {
            if (lists.size() == 1) {
                return lists[0];
            }
            ListNode *back_one = lists.back();
            lists.pop_back();
            ListNode *back_two = lists.back();
            lists.pop_back();
            mergeTwoLists(back_one,back_two,lists);
        }
    }
};
```
