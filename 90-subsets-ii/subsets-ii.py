class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        def f(ind,temp):
            ans.append(temp[:])
            for i in range(ind,len(nums)):
                if i != ind and nums[i]==nums[i-1]:
                    continue
                temp.append(nums[i])
                f(i+1,temp)
                temp.pop()
        ans = []
        nums.sort()
        f(0,[])
        return ans