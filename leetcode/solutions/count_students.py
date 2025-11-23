from typing import List
from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """
        Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
        Output: 0 
        Explanation:
        - Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
        - Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
        - Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
        - Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
        - Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
        - Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
        - Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
        - Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
        Hence all students are able to eat.
        """
        queue = deque(students)
        while queue and sandwiches:
            if queue[0] == sandwiches[0]:
                queue.popleft()
                sandwiches.pop(0)
            else:
                queue.append(queue.popleft())
            if all(student != sandwiches[0] for student in queue):
                break
        return len(queue)
    # Mandatory
