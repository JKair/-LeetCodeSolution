Linked List Cycle II
=========
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?

这个是`Linked List Cycle`的进阶，不过要让我们找到环的起点。

解法：这道题要实现很重要的一个点，就是要明白一条递推公式，我先引用一个图先

![图片啊](http://images.cnitblog.com/blog/354747/201311/05171805-64db9f059a1641e7afaf3dd8223c4fe7.jpg)

这里呢，我们可以推出一条递推式，就是当我们用快慢指针算是否是环的时候，快指针走过的路是a+b+c+b，而慢指针则是a+b。因为快指针跑的速度是慢指针的两倍，那么就有递推式`a+b+c+b = 2(a+b)`，最后我们可以推出`b=c`。这个结论非常重要！谢谢[这个博主](http://blog.sina.com.cn/s/blog_6f611c300101fs1l.html)

1. 首先，我们先找到快慢指针相遇的点，也就是z点
1. 然后我们再让慢指针从新开始(X点)，快指针现在换成步进。
1. 因为`a = c`，所以下一次快慢指针相遇的点，就必定在Y点了

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
    ListNode *detectCycle(ListNode *head) {
        ListNode *slow = head,*fast = head;

        while (fast && fast->next) {
            fast = fast->next->next;
            slow = slow->next;

            if (fast == slow) break;
        }

        if (!fast || !fast->next)  return NULL;

        slow = head;
        while(slow != fast) {
            slow = slow->next;
            fast = fast->next;
        }

        return fast;
    }
};
```

相似题目[Linked List Cycle II](../Easy/Linked List Cycle.md)
