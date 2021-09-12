class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows  = []

        if numRows == 1:
            return s
        
        for i in range(min(len(s), numRows)):
            rows.append("")

        currRow = 0
        goingDown = False

        for c in s:
            rows[currRow] += c
            if(currRow == 0) or currRow == numRows - 1:
                goingDown = not goingDown
            currRow += 1 if goingDown else - 1


        return "".join(rows)

