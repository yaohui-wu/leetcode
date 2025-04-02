class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            num = numbers[left] + numbers[right]
            # Move left pointer to get a greater compliment.
            if num < target:
                left += 1
            # Move right pointer to get a lesser compliment.
            elif num > target:
                right -= 1
            else:
                # Convert from 0-indexed to 1-indexed.
                return [left + 1, right + 1]
        return [0, 0]
