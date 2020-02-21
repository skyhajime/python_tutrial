"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Given:
nums = [2,7,11,15]
target = 9

"""
class TwoSum:
    def twosum(self, nums, target):
        seen = {}
        for index, num in enumerate(nums):
            other = target - num
            if other in seen:
                return [seen[other], index]
            else:
                seen[num] = index

nums = [2,7,11,15]
target = 9
solution = TwoSum()
print(solution.twosum(nums, target))
