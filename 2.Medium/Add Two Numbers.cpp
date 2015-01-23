class Solution {
public:
	ListNode *result = new ListNode(0);
	ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) 
	{
		int token = 0;
		ListNode *head = result;
		ListNode *p = new ListNode(0);
		result->next = p;
		while (l1 != NULL && l2 != NULL)
		{
			result = result->next;
			result->val += l1->val + l2->val;
			token = result->val / 10;
			result->val %= 10;
			if (token != 0)
			{
				ListNode *p = new ListNode(1);
				result->next = p;
				token = 0;
			}
			else if (l1->next != NULL && l2->next != NULL)
			{
				ListNode *p = new ListNode(0);
				result->next = p;
			}
			l1 = l1->next;
			l2 = l2->next;
		}
		while (l1 != NULL)
		{
			if (result->next != NULL)
			{
				result = result->next;
				result->val += l1->val;
				token = result->val / 10;
				result->val %= 10;
				if (token != 0)
				{
					ListNode *p = new ListNode(1);
					result->next = p;
					token = 0;
				}
			}
			else
			{
				ListNode *p = new ListNode(0);
				result->next = p;
				result = result->next;
				result->val += l1->val;
			}
			l1 = l1->next;
		}
		while (l2 != NULL)
		{
			if (result->next != NULL)
			{
				result = result->next;
				result->val += l2->val;
				token = result->val / 10;
				result->val %= 10;
				if (token != 0)
				{
					ListNode *p = new ListNode(1);
					result->next = p;
					token = 0;
				}
			}
			else
			{
				ListNode *p = new ListNode(0);
				result->next = p;
				result = result->next;
				result->val += l2->val;
			}
			l2 = l2->next;
		}
		return head->next;
	}
};