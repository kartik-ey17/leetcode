class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        cur = dummy
        c = 0
        while l1 or l2 or c:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = x+y+c
            c = total//10
            cur.next = ListNode(total%10)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next