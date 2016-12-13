Swap Nodes in Pairs
====================
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

链表交换，将前后两个数字交换。

解法一，这道题我们只交换值都可以ac。

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
    ListNode* swapPairs(ListNode* head) {
        ListNode *temp = head;

        while (temp && temp->next) {
            swap(temp->val, temp->next->val);
            temp = temp->next->next;
        }

        return head;
    }
};
```

解法二，关于树的操作，我们用递归肯定是最舒服的，思路为，将第一个节点看做一个节点，将第二个节点后面一节链表看为第二个节点，然后交换递归（实际上就是回溯了）。

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
    ListNode* swapPairs(ListNode* head) {
        if (!head || !head->next) return head;
        ListNode *temp = head->next;
        head->next = swapPairs(head->next->next);
        temp->next = head;

        return temp;
    }
};
```

解法三，利用迭代去解这道题，在图上画好节点交换的路径，不要把自己都绕晕了就行了。

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
    ListNode* swapPairs(ListNode* head) {
        ListNode *temp = new ListNode(-1), *res = temp;
        temp->next = head;
        while (temp->next && temp->next->next) {
            ListNode *token = temp->next->next;
            temp->next->next = token->next;
            token->next = temp->next;
            temp->next = token;
            temp = token->next;
        }

        return res->next;
    }
};
```
