class Solution:
    def isValid(self, s: str) -> bool:
        open_close = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for c in s:
            if c in open_close:
                stack.append(open_close.get(c))
            elif len(stack) == 0 or stack.pop() != c:
                return False
        return len(stack) == 0
