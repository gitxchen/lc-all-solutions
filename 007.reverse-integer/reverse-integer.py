class Solution(object):
  # def reverse(self, x):
  #   """
  #   :type x: int
  #   :rtype: int
  #   """
  #   sign = x < 0 and -1 or 1
  #   x = abs(x)
  #   ans = 0
  #   while x:
  #     ans = ans * 10 + x % 10
  #     x /= 10
  #   return sign * ans if ans <= 0x7fffffff else 0
  def reverse(self,x):
    sign = x>0 and 1 or -1
    print(sign)
    x =abs(x)
    print(x)
    ans = 0

    while x:
      print(ans)
      ans = ans *10 + x % 10
      x//=10

    return sign * ans if ans <= 0x7fffffff else 0


if __name__ == '__main__':
  s = Solution()

  print(s.reverse(-1234))
