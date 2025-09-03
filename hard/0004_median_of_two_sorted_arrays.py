class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Binary search on the smaller array.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        len1, len2 = len(nums1), len(nums2)
        total_len = len1 + len2
        left, right = 0, len1
        while left <= right:
            # Partition positions.
            partition1 = (left + right) // 2
            partition2 = (len1 + len2 + 1) // 2 - partition1
            # Border values.
            max_left1 = float("-inf") if partition1 == 0 else nums1[partition1 - 1]
            min_right1 = float("inf") if partition1 == len1 else nums1[partition1]
            max_left2 = float("-inf") if partition2 == 0 else nums2[partition2 - 1]
            min_right2 = float("inf") if partition2 == len2 else nums2[partition2]
            # Valid partition found.
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if total_len % 2 == 0:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0
                else:
                    return max(max_left1, max_left2)
             # Adjust binary search.
            elif max_left1 > min_right2:
                right = partition1 - 1
            else:
                left = partition1 + 1
