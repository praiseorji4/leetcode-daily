class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # # Using a hashmap
        # hashmap = {} # To store the the digit additions

        # # since nums.length can equal 1
        # if len(nums) == 1:
        #     return - 1 # As there wold be no possible combimations

        # for num in nums:
        #     num_of_digits = len(str(num))
        #     idx = 0
        #     for i in range(len(num_of_digits)):
        #         idx += int(str(num)[i])
            
        #     hashmap 
        digit_sum_map = defaultdict(list)
    
        # group numbers by their digit sum
        for num in nums:
            digit_sum = sum(int(digit) for digit in str(num))
            digit_sum_map[digit_sum].append(num)
        
        max_sum = -1
        
        # find the maximum sum for each group
        for key in digit_sum_map:
            if len(digit_sum_map[key]) > 1:
                digit_sum_map[key].sort(reverse=True)
                max_sum = max(max_sum, digit_sum_map[key][0] + digit_sum_map[key][1])
        
        return max_sum