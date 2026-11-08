class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max(nums)
        cur_max = 1
        cur_min = 1
        for i in nums:
            t = cur_max*i
            cur_max = max(t,cur_min*i,i)
            cur_min = min(t,cur_min*i,i)
            res = max(res,cur_max)
        return res