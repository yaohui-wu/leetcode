class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [1] * length
        prefix_products = [1] * length
        product = 1
        for i in range(length):
            product *= nums[i]
            prefix_products[i] = product
        suffix_products = [1] * length
        product = 1
        for i in range(length - 1, -1, -1):
            product *= nums[i]
            suffix_products[i] = product
        answer[0] *= suffix_products[1]
        answer[length - 1] *= prefix_products[length - 2]
        for i in range(1, length - 1):
            answer[i] *= prefix_products[i - 1] * suffix_products[i + 1]
        return answer
