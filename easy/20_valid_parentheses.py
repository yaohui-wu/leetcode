class Solution:
    def isValid(self, s: str) -> bool:
        open_close = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for c in s:
            # If C is an open bracket, push the corresponding close bracket to
            # the stack.
            if c in open_close:
                stack.append(open_close.get(c))
            # If C is a close bracket, check if the stack is empty or the top
            # of the stack is the same close bracket.
            elif len(stack) == 0 or stack.pop() != c:
                return False
        # If the stack is empty, then all the brackets are balanced.
        return len(stack) == 0
