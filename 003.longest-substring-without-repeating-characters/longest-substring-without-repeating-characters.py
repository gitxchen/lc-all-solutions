# class Solution(object):
#   def _lengthOfLongestSubstring(self, s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     d = collections.defaultdict(int)
#     l = ans = 0
#     for i, c in enumerate(s):
#       while l > 0 and d[c] > 0:
#         d[s[i - l]] -= 1
#         l -= 1
#       d[c] += 1
#       l += 1
#       ans = max(ans, l)
#     return ans
#
#   def lengthOfLongestSubstring(self, s):
#     d = {}
#     start = 0
#     ans = 0
#     for i, c in enumerate(s):
#       if c in d:
#         start = max(start, d[c] + 1)
#       d[c] = i
#       ans = max(ans, i - start + 1)
#     return ans

class Solution(object):


  def lengthOfLongestSubstring(self, s):
    left = 0
    d = {}
    res = 0
    for i, c in enumerate(s):
      if c in d and d[c] >= left:
        left = d[c]+1
      d[c] = i
      res = max(res, i - left + 1)
    return res


if __name__ == '__main__':
  s = Solution()
  ss = 'abcabcbb'
  #print(s.lengthOfLongestSubstring(ss))







































class Solution(object):
  def lengthOfLongestSubstring(self,s):
    d=[-1] * 256
    left = -1
    res = 0
    for i, letter in enumerate(s):
      left = max(left,d[ord(letter)])
      res = max(res, i - left)
      d[ord(letter)] = i
    return res

if __name__ == '__main__':
  s = Solution();
  print(s.lengthOfLongestSubstring("bdcdd"))


