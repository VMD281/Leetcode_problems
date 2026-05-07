class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])

        for x in range(m):
            i  = n - 1
            c = i
            while c >= 0:
                if box[x][c] == ".":
                    c -= 1

                elif box[x][c] == "*":
                    c -= 1
                    i = c

                elif box[x][c] == "#":
                    box[x][c] = "." 
                    box[x][i] = "#"
                    c -= 1
                    i -= 1
        
        rotated = [[0] * m for _ in range(n)]

        for r in range(m):
            for c in range(n):
                rotated[c][m - 1 - r] = box[r][c]

        return rotated