def find_duplicate(nums):

    if not nums:
        return 0
    read_idx =0
    write_idx =0
    n = len(nums)
    duplicates =[]

    while read_idx <n:
        if read_idx <n-1 and nums[read_idx] == nums[read_idx+1]:
            val = nums[read_idx]
            duplicates.append(val)
            while read_idx<n and val == nums[read_idx]:
                read_idx +=1
        else:
            nums[write_idx] = nums[read_idx]
            write_idx +=1
            read_idx +=1       
    return duplicates

arr = [1,2,2,2,3,3,4,5,5]
result = find_duplicate(arr)
print (result)            

