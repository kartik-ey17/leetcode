def longestConsecutive(nums):
    n_set = set(nums)
    longest = 0

    for num in n_set:
        if num-1 not in n_set:
            curr = num
            length = 1

            while curr+1 in n_set:
                curr += 1
                length += 1

            longest = max(longest,length)
    return longest