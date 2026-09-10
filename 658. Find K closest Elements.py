def findClosestElements(arr,k,x):
    l = 0
    r = len(arr)-k
    while l<r:
        mid = l + (r-l)//2
        if x - arr[mid] > arr[mid+k] - x:
            l = mid + 1
        else:
            r = mid
    return arr[l:l+k]
print(findClosestElements([1,1,2,3,4,5] , 4 , -1))