# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 19:38:30 2018

@author: wwl
"""

class Solution:
    """
    给定一个整数数组 nums 和一个目标值 target，
    请你在该数组中找出和为gai目标值的 两个 整数。
    你可以假设每种输入只会对应一个答案。
    但是，你不能重复利用这个数组中同样的元素。
    """
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        numLength = len(nums)
        result = list()
        for index in range(numLength):
            num1 = target - nums[index]
            for index1 in range(index+1,numLength):
                if num1 == nums[index1]:
                    result.append(index)
                    result.append(index1)
        return result
    def twoSumHashmap(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapData = {}
        for index in range(len(nums)):
            num1 = target - nums[index]
            index1 = mapData.get(num1,-1)
            if index1 >= 0:
                result = [index,index1]
                result.sort()
                return result
            mapData[nums[index]] = index 
        return []
            
    
if __name__ == "__main__":
    obj = Solution()
    print(obj.twoSum([2, 7, 11, 15],9))
    print(obj.twoSumHashmap([2, 7, 11, 15],9))
 
    

                