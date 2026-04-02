class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # two pointer/sliding window approach -> O(2k)    s: O(1)
        lsum = 0
        rsum = 0
        rindex = len(cardPoints) - 1
        maxPoints = 0
        for i in range(k):
            lsum += cardPoints[i]
        maxPoints = lsum
        for i in range(k-1, -1, -1):
            lsum -= cardPoints[i]
            rsum += cardPoints[rindex]
            maxPoints = max(maxPoints, lsum + rsum)
            rindex -= 1
        return maxPoints

