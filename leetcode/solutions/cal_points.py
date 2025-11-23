from typing import List
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # for x in operations:
        #     if x == 'C':
        #         operations.pop()
        #     elif x == 'D':
        #         operations.append(2 * operations[-1])
        #     elif x == "+":
        #         operations.append(operations[-2] + operations[-1])
        #     else:
        #         operations.append(x)
        stack = []
        for x in operations:
            try:
                stack.append(int(x))
                # print(stack)
            except ValueError:
                if x == 'C':
                    stack.pop()
                    # print(stack)
                elif x == 'D':
                    stack.append(stack[-1] * 2)
                    # print(stack)
                elif x == '+':
                    stack.append(stack[-1] + stack[-2])
                    # print(stack)
        return sum(stack)
        