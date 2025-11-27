class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count, number, index = 0, 1, 0
        n = len(arr)
        while count < k:
            if index < n and arr[index] == number:
                index += 1
            else:
                count += 1
                if count == k:
                    return number
            number += 1
        return (-42)