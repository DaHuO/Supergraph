#method 1: two pointers
class Solution:
	def minSubArrayLen(self, s, nums):
		sum = 0
		res = float('inf')
		head = 0

		for i in range(len(nums)):
			sum += nums[i]

			while sum >= s:
				res = min(res, i - head + 1)
				sum -= nums[head]
				head += 1

		return res if res <= len(nums) else 0

		