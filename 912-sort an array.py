def sortArray(nums):
    def mergesort(arr):
        if len(arr) <= 1:
            return arr
        arrL = mergesort(arr[:len(arr)//2])
        arrR = mergesort(arr[len(arr)//2:])

        return merge(arrL,arrR)
    def merge(arrL,arrR):
        r = []
        i=0
        j=0

        while i < len(arrL) and j < len(arrR):
            if arrL[i] < arrR[j]:
                r.append(arrL[i])
                i += 1
            else:
                r.append(arrR[j])
                j += 1
        r.extend(arrL[i:])
        r.extend(arrR[j:])
        return r
    return mergesort(nums)
print(sortArray([]))