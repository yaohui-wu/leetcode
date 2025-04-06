class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0 # Number of subarrays with sum equal to k.
        sum = 0 # Running sum of the elements.
        # Hash map to store frequency of different prefix sums.
        sum_to_count = {0: 1} # Handle single element subarrays.
        for i in nums:
            sum += i
            # If the difference has been seen before, it means there exists a
            # subarray ending at the current index whose sum is k.
            count += sum_to_count.get(sum - k, 0)
            sum_to_count[sum] = sum_to_count.get(sum, 0) + 1
        return count
