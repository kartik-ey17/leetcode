def intersection(nums1,nums2):
    hmap = {}
    output = []
    for i,n in enumerate(nums1):
        hmap[n] = i
    for i,n in enumerate(nums2):
        if n in hmap and n not in output :
            output.append(n)
            continue
    return output

print(intersection([4,9,5] , [9,4,9,8,4]))