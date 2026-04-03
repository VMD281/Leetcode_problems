class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        r = 0
        maxfruits = 0
        hashmap = {}

        for r in range(len(fruits)):
            if fruits[r] not in hashmap:
                if len(hashmap) < 2:
                    hashmap[fruits[r]] = 1    #adding a new key
                    maxfruits = max(maxfruits, sum(hashmap.values()))
                else:
                    while len(hashmap) >= 2:
                        hashmap[fruits[l]] -= 1
                        if hashmap[fruits[l]] == 0:
                            del hashmap[fruits[l]]
                        l += 1
                    hashmap[fruits[r]] = 1
                    maxfruits = max(maxfruits, sum(hashmap.values()))

            else:
                hashmap[fruits[r]] += 1
                maxfruits = max(maxfruits, sum(hashmap.values()))
        return maxfruits


