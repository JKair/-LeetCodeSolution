//递归严重超时
class Solution {
public:
	int climbStairs(int n) 
	{
		if (n == 1 || n == 2)
			return n == 1 ? 1 : 2;
		return climbStairs(n - 1) + climbStairs(n - 2);
	}
};

//于是我使用了迭代
class Solution {
public:
	int climbStairs(int n) 
	{
		if (n<= 2)
			return n;
		
		int* step = new int[n];
		step[0] = 1;
		step[1] = 2;
		for (int i = 2; i < n; i++)
		{
			step[i] = step[i - 1] + step[i - 2];
		}
		return step[n - 1];
	}
};