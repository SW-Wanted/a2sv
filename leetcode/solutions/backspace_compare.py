class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for x in s:
            try:
                if x.lower() >= 'a' and x <= 'z':
                    stack1.append(x)
                else:
                    raise ValueError
            except ValueError:
                if x == '#' and len(stack1) > 0:
                    stack1.pop()
        for x in t:
            try:
                if x.lower() >= 'a' and x <= 'z':
                    stack2.append(x)
                else:
                    raise ValueError
            except ValueError:
                if x == '#' and len(stack2) > 0:
                    stack2.pop()
        return stack1 == stack2
    # Mandatory
