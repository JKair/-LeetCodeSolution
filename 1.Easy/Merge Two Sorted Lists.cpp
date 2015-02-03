class Solution {
public:
	ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) 
	{
		ListNode *result = new ListNode(-1);
		ListNode *p = result;
		if (!l1 || !l2)
		{
			return !l1 ? l2 : l1;
		}
		while (l1 || l2)
		{
			if (l1 && l2 && l1->val <= l2->val)
			{
				result->next = new ListNode(l1->val);
				l1 = l1->next;
				result = result->next;
				continue;
			}
			else if (l1 && l2 && l1->val > l2->val)
			{
				result->next = new ListNode(l2->val);
				l2 = l2->next;
				result = result->next;
				continue;
			}
			if (!l1 &&!l2)
			{
				break;
			}
			if (l1)
			{
				result->next = new ListNode(l1->val);
				l1=l1->next;
				result = result->next;
				continue;
			}
			if (l2)
			{
				result->next = new ListNode(l2->val);
				l2 = l2->next;
				result = result->next;
			}
		}
		return p->next;
	}
};