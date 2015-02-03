class Solution {
public:
	bool isValid(string s) {
		vector<char> v;
		for (int i = 0; i < s.length(); i++)
		{
			if (s[i] == '{' || s[i] == '(' || s[i] == '[')
			{
				v.push_back(s[i]);
				continue;
			}
			if (v.empty())
			{
				return false;
			}
			if (s[i] - v.back() <= 2)
			{
				v.pop_back();
			}
			else
			{
				return false;
			}
		}
		return v.empty();
	}
};