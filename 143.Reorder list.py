def reorderList(head):
    if not head or not head.next:
        return
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    second = slow.next
    slow.next = None

    prev = None
    while second:
        nxt = second.next
        second.next = prev
        prev = second
        second = nxt
    second = prev

    while second:
        t1 = first.next
        t2 = second.next
        first.next = second
        second.next = t1
        first = t1
        second = t2