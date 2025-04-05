class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [1] * length
        # Compute the prefix products.
        for i in range(1, length):
            answer[i] = answer[i - 1] * nums[i - 1]
        # Compute the suffix products.
        product = 1
        for i in range(length - 2, -1, -1):
            product *= nums[i + 1]
            answer[i] *= product
        return answer
