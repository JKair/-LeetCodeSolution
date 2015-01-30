class Solution {
public:
	ListNode *deleteDuplicates(ListNode *head)
	{
		if (head == NULL || head->next == NULL)
		{
			return head;
		}
		ListNode *p = head;
		while (p&&p->next)
		{
			if (p->next->val == p->val)
			{
				p->next = p->next->next;
			}
			else
			{
				p = p->next;
			}
		}
		return head;
	}
};