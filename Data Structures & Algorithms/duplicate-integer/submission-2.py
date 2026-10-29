class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       #intialise set
       seen = set()
      
       for num in nums:
        #if the num is in the set, a duplicate exists
        if num in seen:
            return True
        seen.add(num)
       return False