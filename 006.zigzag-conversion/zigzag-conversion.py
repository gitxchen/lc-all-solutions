class Solution(object):
  # def convert(self, s, numRows):
  #   """
  #   :type s: str
  #   :type numRows: int
  #   :rtype: str
  #   """
  #   if numRows <= 1:
  #     return s
  #   n = len(s)
  #   ans = []
  #   step = 2 * numRows - 2
  #   for i in range(numRows):
  #     one = i
  #     two = -i
  #     while one < n or two < n:
  #       if 0 <= two < n and one != two and i != numRows - 1:
  #         ans.append(s[two])
  #       if one < n:
  #         ans.append(s[one])
  #       one += step
  #       two += step
  #   return "".join(ans)

  def convert(self, s, numRows):
    ans = []
    n = len(s)
    if numRows <= 1:
      return s

    if n % (2*numRows -2) <= numRows:
      numCols = n // (2*numRows -2) *2 + 1
    else:
      numCols = n // (2 * numRows - 2) *2+ 2

    print(numCols)

    for i in range(numRows):
      print('i: ', int(i))
      for j in range(numCols):
        if (i == 0 or i == numRows -1) and (j%2 ==1):
          continue
        else:
          if j%2 == 0:
            ind = (j // 2) * (2 * numRows - 2) + i
          else:
            ind = (j//2) * (2* numRows -2) + numRows + numRows-1 -i -1
          if ind < n:
            ans.append(s[ind])

    return "".join(ans)


          
if __name__ == '__main__':
  s = Solution()
  str = "abcdefghijklmn"
  numRows = 3
  print(s.convert(str, numRows))

