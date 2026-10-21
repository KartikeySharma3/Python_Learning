def remove_all_duplicates(nums):
    if not nums:
        return 0

    write_idx = 0
    read_idx = 0
    n = len(nums)

    while read_idx < n:
        # Check if the current element has duplicates ahead
        if read_idx < n - 1 and nums[read_idx] == nums[read_idx + 1]:
            val = nums[read_idx]
            # Fast-forward past ALL identical copies
            while read_idx < n and nums[read_idx] == val:
                read_idx += 1
        else:
            # Strictly unique element
            nums[write_idx] = nums[read_idx]
            write_idx += 1
            read_idx += 1

    return write_idx

# Test run
arr = [1, 2, 2, 3, 3, 4, 6, 9]
k = remove_all_duplicates(arr)
print(f"k = {k}")
print(f"Remaining: {arr[:k]}")  # Output: [1, 4, 6, 9]