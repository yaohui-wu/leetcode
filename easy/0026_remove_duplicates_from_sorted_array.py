class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0 # Index of the last unique element.
        for i in range(1, len(nums)):
            # Insert the next unique element.
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]
        # Return the length of the unique elements.
        return k + 1
