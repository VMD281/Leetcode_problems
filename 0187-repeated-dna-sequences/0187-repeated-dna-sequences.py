class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        repeated = set()
        j = 0
        for i in range(len(s)):
            j = i + 9
            if s[i:j+1] in seen:
                if s[i:j+1] not in repeated:
                    repeated.add(s[i:j+1])
            else:
                seen.add(s[i:j+1])
        return list(repeated)