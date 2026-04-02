class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        curlen = 0
        maxlen = 0
        zeros = 0
        while r < len(nums):
            if nums[r] == 0:
                zeros += 1
            if zeros <= k:
                curlen = r-l+1
                maxlen = max(maxlen, curlen)
            else:
                while zeros > k:
                    if nums[l] == 0:
                        zeros -= 1 
                    l += 1
                curlen = r-l+1
                maxlen = max(maxlen, curlen)
            r += 1
        return maxlen
            
