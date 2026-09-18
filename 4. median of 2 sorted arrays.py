def findMedianSortedArrays(nums1,nums2):
    if len(nums1) > len(nums2):
        nums1,nums2 = nums2,nums1
    m = len(nums1)
    n = len(nums2)

    l = 0
    r = m
    while l <= r:
        i = (l+r) // 2
        j = (m+n+1) // 2 -i

        al = float("-inf") if i == 0 else nums1[i - 1]
        ar = float("-inf") if i == m else nums1[i]

        bl = float("-inf") if j == 0 else nums2[j-i]
        br = float("inf") if j == n else nums2[j]
        if al <= br and bl <= ar:
            if (m+n)%2:
                return max(al,bl)
            return max(al,bl) + min(ar,br)/2
        elif al > br:
            r = i-1
        else:
            l = i+1