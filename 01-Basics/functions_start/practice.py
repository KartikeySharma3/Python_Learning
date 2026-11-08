def two_sum(nums, target):
    seen ={}

    for idx, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], idx], [complement, num]

        seen[num] = idx

    return[]

nums = [3,6,7,2]
target = 9
result = two_sum(nums, target)

print(f"the two sums of the given list:{result}")