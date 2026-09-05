class Solution(object):
    def rotate(self, nums, k):
       if not nums:
           return 
       
       k %=len(nums)
       nums[:] = nums[-k:] + nums[:-k]
       return nums[:]
