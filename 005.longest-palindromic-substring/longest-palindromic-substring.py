class Solution(object):
  # def longestPalindrome(self, s):
  #   """
  #   :type s: str
  #   :rtype: str
  #   """
  #   left = right = 0
  #   n = len(s)
  #   for i in range(n - 1):
  #     if 2 * (n - i) + 1 < right - left + 1:
  #       break
  #     l = r = i
  #     while l >= 0 and r < n and s[l] == s[r]:
  #       l -= 1
  #       r += 1
  #     if r - l - 2 > right - left:
  #       left = l + 1
  #       right = r - 1
  #     l = i
  #     r = i + 1
  #     while l >= 0 and r < n and s[l] == s[r]:
  #       l -= 1
  #       r += 1
  #     if r - l - 2 > right - left:
  #       left = l + 1
  #       right = r - 1
  #   return s[left:right + 1]
  def longestPalindrome(self, s):
    left = right = 0
    n=len(s)
    i = 0
    while i < n:
      if (n-i+1)*2 < right -left +1:
        break
      l = r = i
      while r < n-1 and s[r] == s[r+1]:
          r=r+1
      i = r+1
      while l>=0 and r < n and s[l] == s[r]:
        l=l-1
        r=r+1
      if r-l-2 > right -left:
        left = l+1
        right = r-1

    return s[left:right+1]


if __name__ == '__main__':
  s = Solution()
  str='bnooonooo'
  print(s.longestPalindrome(str))
