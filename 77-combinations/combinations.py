class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        ans = []
        def f(i,ans,curr):
            if len(curr) > k:
                return
            if i==n:
                if len(curr) == k:
                    ans.append(curr.copy())
                return
            curr.append(i+1)
            f(i+1,ans,curr)
            curr.pop()
            f(i+1,ans,curr)
        f(0,ans,[])
        return ans