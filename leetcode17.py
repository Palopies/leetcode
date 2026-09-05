class Solution(object):
    def firstMissingPositive(self, nums):
      #  hash_set = set(nums)
       # n = len(nums)
       # for i in range(1,n+2):
        #    if i not in hash_set:
         #       return i 
        hash_dict = {}
        for num in nums:
          hash_dict[num] = 1
        
        for i in range(1,len(nums)+2):
          if i not in hash_dict:
            return i