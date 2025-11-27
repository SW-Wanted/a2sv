class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        result = [0] * n
        
        for i in range(n):
            for j in range(n):
                if boxes[j] == '1' and i != j:
                    result[i] += abs(i - j)

        return result