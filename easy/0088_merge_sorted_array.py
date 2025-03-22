class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m + n - 1 # Current index to insert.
        # Iterate from the end of both arrays.
        while m > 0 and n > 0:
            # Insert the lesser number to the end of nums1.
            num1 = nums1[m - 1]
            num2 = nums2[n - 1]
            if num1 < num2:
                nums1[i] = num2
                n -= 1
            else:
                nums1[i] = num1
                m -= 1
            i -= 1
        # Copy the remaining elements of nums2 to the front of nums1.
        for i in range(n):
            nums1[i] = nums2[i]
