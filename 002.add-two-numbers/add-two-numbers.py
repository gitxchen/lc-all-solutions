# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution(object):
  # maybe standard version
#  def _addTwoNumbers(self, l1, l2):
#    """
#    :type l1: ListNode
#    :type l2: ListNode
#    :rtype: ListNode
#    """
#    p = dummy = ListNode(-1)
#    carry = 0
#    while l1 and l2:
#      p.next = ListNode(l1.val + l2.val + carry)
#      carry = p.next.val / 10
#      p.next.val %= 10
#      p = p.next
#      l1 = l1.next
#      l2 = l2.next
#
#    res = l1 or l2
#    while res:
#      p.next = ListNode(res.val + carry)
#      carry = p.next.val / 10
#      p.next.val %= 10
#      p = p.next
#      res = res.next
#    if carry:
#      p.next = ListNode(1)
#    return dummy.next
#
#  # shorter version
#  def addTwoNumbers(self, l1, l2):
#    p = dummy = ListNode(-1)
#    carry = 0
#    while l1 or l2 or carry:
#      val = (l1 and l1.val or 0) + (l2 and l2.val or 0) + carry
#      carry = val / 10
#      p.next = ListNode(val % 10)
#      l1 = l1 and l1.next
#      l2 = l2 and l2.next
#      p = p.next
#    return dummy.next

  def addTwoNumbers(self, l1, l2):
    p = dummyhead = ListNode(-1)
    carry = 0
    while l1 or l2 or carry:
      val = (l1 and l1.val or 0) + (l2 and l2.val or 0) + carry
      print("val: ", val)
      carry = int(val / 10)
      print("carry: ", carry)
      p.next = ListNode(val % 10)
      if l1:
        l1 = l1.next
      if l2:
        l2 = l2.next
      #l1 = l1 and l1.next
      #l2 = l2 and l2.next
      p = p.next
    return dummyhead.next

if __name__ == '__main__':
  l1 = ListNode(1)
  l1.next =ListNode(2)
  l1.next.next = ListNode(3)

  l2 = ListNode(3)
  l2.next = ListNode(1)
  l2.next.next = ListNode(9)

  s = Solution()
  print('ok')
  res = s.addTwoNumbers(l1,l2)

  print(res.val)
  print(res.next.val)
  print(res.next.next.val)
