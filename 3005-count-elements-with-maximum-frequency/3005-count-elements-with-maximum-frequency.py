class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        f = collections.Counter(nums)
        mx = max(f.values())

        c=0
        for x in nums:
            if f[x] == mx:
                c += 1

        return c   
