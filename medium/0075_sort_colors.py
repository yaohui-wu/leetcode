class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Three-way partitioning in Dutch national flag problem.
        # 0 (red) is at the left, 1 (white) is in the middle, and 2 (blue) is
        # at the right.
        i = 0 # Boundary for 0 (red).
        j = 0 # Current element.
        k = len(nums) - 1 # Boundary for 2 (blue).
        while j <= k:
            if nums[j] < 1:
                # 0 (red), swap it to the "0" section.
                self.swap(nums, i, j)
                i += 1
                j += 1
            elif nums[j] > 1:
                # 2 (blue), swap it to the "2" section.
                self.swap(nums, j, k)
                k -= 1
            else:
                # 1 (white), it's already in the middle, move j forward.
                j += 1
    
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
