from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            row = [1] * (i + 1)
            # print(f'i={i}')
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
                # print(f'   {triangle[i - 1][j - 1]} + {triangle[i - 1][j]}-> row[{j}]={row[j]}')
            triangle.append(row)
        return triangle