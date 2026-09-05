from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        '''行'''
        row = 0
        '''列'''
        col = len(matrix[0])-1
        while row<len(matrix) and col >=0:
            cul = matrix[row][col]
            if cul ==target:
                return True
            elif cul> target:
                col -=1
            else:
                row +=1
        return False;