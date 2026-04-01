class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        hashset = set()
        for i in range(n+1):
            hashset.add(i)
        for i in range(len(nums)):
            if nums[i] in hashset:
                hashset.remove(nums[i]) 
        if hashset:
            l = list(hashset)
            return l[0]

        # Brute force solution - TC: O(n)
        # for i in range(0, n + 1):
        #     flag = 0
        #     for j in range(0, n):
        #         if nums[j] == i:
        #             flag = 1
        #             break
        #     if flag == 0:
        #         return i
        
        
        # Better Solution - TC: O(n) SC: O(n)
        # hashmap = {}
        # for num in nums:
        #     hashmap[num] = 1
        # for i in range(0, n + 1):
        #     if i not in hashmap:
        #         return i


        # Optimal solution :1 - TC: O(2n) SC: O(1)
        # totalsum = n*(n+1)//2
        # tempsum = 0 
        # for num in nums:
        #     tempsum += num
        
        # return (totalsum - tempsum)

        # More optimal solution - Using XOR - TC: O(n)  
        # XOR1 = 0
        # XOR2 = 0
        # for i in range(n):
        #     XOR1 = XOR1 ^ (i + 1)
        #     XOR2 = XOR2 ^ nums[i]
        # return XOR1 ^ XOR2

