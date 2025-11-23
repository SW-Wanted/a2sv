class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for x in s:
            try:
                if x.isalpha():
                    stack.append(x)
                else:
                    raise ValueError
            except ValueError:
                if x.isalnum() and len(stack):
                    stack.pop()
        return "".join(stack)
# Mandatory
