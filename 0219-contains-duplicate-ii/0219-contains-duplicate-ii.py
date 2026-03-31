class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # brute force
        # if len(nums) < 2:
        #     return False

        # if k == 0:
        #     return False

        # i = 0
        # j = 1
        # while i < len(nums):
        #     j = i + 1
        #     while abs(i - j) <= k and j < len(nums):
        #         if nums[i] == nums[j]:
        #             return True

        #         else:
        #             j += 1  

        #     i += 1

        # return False
        hashmap = {}

        for i in range(len(nums)):
            if nums[i] in hashmap:
                if abs(hashmap[nums[i]] - i) <= k:
                    return True
                else: #update
                    hashmap[nums[i]] = i
            else: #add new
                hashmap[nums[i]] = i
        return False
