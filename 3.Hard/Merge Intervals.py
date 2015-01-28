class Solution:
	def merge(self, intervals):
		if not intervals:
			return  []
		intervals.sort(key=lambda x:x.start)
		result = [intervals[0],]
		for token in intervals:
			if result[-1].end >= token.start:
				result[-1].end = max(token.end,result[-1].end)
			else:
				result.append(token)
		return result