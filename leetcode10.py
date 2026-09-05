class Solution(object):
    def subarraySum(self, nums, k):
        pre_sum = 0
        res = 0
        mp = {0: 1}
        
        