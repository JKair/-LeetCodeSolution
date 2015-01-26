class Solution {
public:
	ListNode *swapPairs(ListNode *head) {
		if (!head || !head->next)
		{
			return head;
		}
		ListNode *token = head;
		while (token && token->next)
		{
			int swap = token->val;
			token->val = token->next->val;
			token->next->val = swap;
			token = token->next->next;
		}
		return head;
	}
};