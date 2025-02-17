class Solution:
    def isValid(self, s: str) -> bool:
        close_open = {")": "(", "}": "{", "]": "["}
        stack = []
        for c in s:
            if c in close_open.values():
                stack.append(c)
            elif len(stack) == 0:
                return False
            elif stack.pop() != close_open.get(c):
                return False
        return len(stack) == 0
