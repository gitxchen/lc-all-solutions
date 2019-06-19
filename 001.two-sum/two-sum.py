class Solution(object):
  def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    d = {}
    for i, num in enumerate(nums):
      if target - num in d:
        return [d[target - num], i]
      d[num] = i
    # no special case handling because it's assumed that it has only one solution

if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.twoSum([3, 2, 4], 6))