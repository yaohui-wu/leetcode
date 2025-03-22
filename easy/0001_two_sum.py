class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {} # Map the integer in the list to its index.
        for i in range(len(nums)):
            complement = target - nums[i]
            # Complement is found in elements before the current element.
            if complement in num_to_index:
                # Return the index of the complement and the current element.
                return [num_to_index[complement], i]
            # Add the current element to the hash table.
            num_to_index[nums[i]] = i
        # Renturn an empty list if no solution is found.
        return []
