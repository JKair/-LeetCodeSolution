class Solution {
public:
	bool hasCycle(ListNode *head) {
		if (!head || !head->next)
		{
			return false;
		}
		ListNode *token_a = head;
		ListNode *token_b = head->next;
		while (token_a && token_b && token_b->next)
		{
			token_a = token_a->next;
			token_b = token_b->next->next;
			if (token_a == token_b)
			{
				return true;
			}
		}
		return false;
	}
};