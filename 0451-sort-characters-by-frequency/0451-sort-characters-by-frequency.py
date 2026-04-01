class Solution:
    def frequencySort(self, s: str) -> str:
        freq = [[] for _ in range(len(s) + 1)]
        # 0  1       2    3 4
           #[t, r]  [e]
        hashmap = {}
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = 1
            else:
                hashmap[s[i]] += 1

        for key, val in hashmap.items():
            freq[val].append(key)
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for ch in freq[i]:
                result.append(ch * i)

        return "".join(result)

