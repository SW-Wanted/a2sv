from typing import List
from collections import deque

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # tickets = [2,3,2], k = 2
        """
        The queue starts as [2,3,'2'], where the kth person is 'underlined'.
        After the person at the front has bought a ticket, the queue becomes [3,'2',1] at 1 second.
        Continuing this process, the queue becomes ['2',1,2] at 2 seconds.
        Continuing this process, the queue becomes [1,2,'1'] at 3 seconds.
        Continuing this process, the queue becomes [2,'1'] at 4 seconds. Note: the person at the front left the queue.
        Continuing this process, the queue becomes ['1',1] at 5 seconds.
        Continuing this process, the queue becomes [1] at 6 seconds. The kth person has bought all their tickets, so return 6.
        """
        time = 0
        queue = deque([(i, tickets[i]) for i in range(len(tickets))])
        while queue:
            person, ticket = queue.popleft()
            ticket -= 1
            time += 1
            if ticket == 0 and person == k:
                return time
            if ticket > 0:
                queue.append((person, ticket))
        return 0
        # Mandatory
