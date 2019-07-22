class Solution(object):
  # def findMedianSortedArrays(self, nums1, nums2):
  #   a, b = sorted((nums1, nums2), key=len)
  #   m, n = len(a), len(b)
  #   after = (m + n - 1) / 2
  #   lo, hi = 0, m
  #   while lo < hi:
  #     i = (lo + hi) / 2
  #     if after - i - 1 < 0 or a[i] >= b[after - i - 1]:
  #       hi = i
  #     else:
  #       lo = i + 1
  #   i = lo
  #   nextfew = sorted(a[i:i + 2] + b[after - i:after - i + 2])
  #   return (nextfew[0] + nextfew[1 - (m + n) % 2]) / 2.0



  def findMediaSortedArrays(self,nums1, nums2):
    m=len(nums1)
    n=len(nums2)

    return (findKth(nums1, m/2, nums2, n/2, (m+n+1)/2) + findKth(nums1, m/2, nums2, n/2, (m+n+2)/2))/2.0


    midVal1 = nums1[m/2]
    midVal2 = nums2[n/2]

    if (midVal1 < midVal2) :

      computeNext(nums1, m/2, nums2, n/2)





    
