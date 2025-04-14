class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two pointers.
        i = 0 # Left pointer.
        j = len(s) - 1 # Right pointer.
        while i < j:
            # Skip non-alphanumeric characters.
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            else:
                # Compare lower case alphanumeric characters.
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1
        return True
