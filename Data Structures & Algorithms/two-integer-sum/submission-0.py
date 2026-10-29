class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # initialise dict
        num_ind = {}
        # make the value the key, easier for lookup
        for i, val in enumerate(nums):
            num_ind[val] = i
        # find the difference between the target and current value, find if that difference exists within the dict
        for i, val in enumerate(nums):
            difference = target - val
            if difference in num_ind and num_ind[difference] != i:
                return [i, num_ind[difference]]
        return []
