class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n

        left_product = 1
        '''这个函数的思想很典型，顺序的执行但是又需要记录每一步骤的结果，就不需要暴力每一个位置的结果，定义一个
        负责记录的，这一步骤可以复用上一步骤的结果
        '''
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(n-1, -1 , -1):
            answer[i] *= right_product
            right_product *= nums[i]
        return answer

