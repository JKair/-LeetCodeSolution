class Solution {
public:
	ListNode *removeNthFromEnd(ListNode *head, int n) 
	{		
		ListNode *p = head;
		if (depth(p) < n)
		{
			return head;
		}
		else if (depth(p)==n)
		{
			return head->next;
		}
		else
		{
			while (depth(p) != n + 1)
			{
				p = p->next;
			}
			p->next = p->next->next;
			return head;
		}
	}

	int depth(ListNode *p)
	{
		return !p->next ? 1 : depth(p->next) + 1;
	}
};