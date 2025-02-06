class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        prod_dict = {}

        res = 0
        for i in range(len(nums)): # Get all possible products
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                prod_dict[product] = prod_dict.get(product, 0) + 1 # Number of times each product appears

        
        for count in prod_dict.values():
            pairs = (count * (count - 1)) // 2 # Number of pairs
            res += 8 * pairs # For each pair, we have 8 permutations
        return res