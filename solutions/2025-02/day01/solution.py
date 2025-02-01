class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Thought Process:
        # List of lists method where the frequency is the of each element is represented 
        # by their index in the array.
        # Hence, top frequent would just be getting the elements from the back of the arry
        # Since we've been assured that the answers are unique, this should work

        # Get the counts of each ele
        count_dict = {}

        for num in nums:
            count_dict[num] = 1 + count_dict.get(num, 0)

        # Put counts in a list and sort by count
        count_array = []
        for num, count in count_dict.items():
            count_array.append([count, num]) # Putting count first so that sort uses it
        
        # Makes things O(nlogn)
        count_array.sort() # Largest frequency is behind

        res = []
        for i in range(k):
            res.append(count_array.pop()[1]) # Get the number not the count

        return res