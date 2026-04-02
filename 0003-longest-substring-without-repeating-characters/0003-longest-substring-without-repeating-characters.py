class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        l = 0
        r = 0
        longeststring = 0
        for r in range(len(s)):
            if s[r] not in hashmap:
                curlength = r-l+1
                longeststring = max(longeststring, curlength)
                hashmap[s[r]] = r
            else:
                l = max(l, hashmap[s[r]] + 1)
                hashmap[s[r]] = r
                curlength = r-l+1
                longeststring = max(longeststring, curlength)
        return longeststring
            