class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0 # Size of the array of elements that are not equal to val.
        for i in range(len(nums)):
            # Move elements that are not equal to val to the front.
            if nums[i] != val:
                if i != k:
                    nums[k] = nums[i]
                k += 1
        return k
