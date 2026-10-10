def two_sum(nums,target):
    seen = {}
    
    for idx,num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return[seen[complement],idx]
        else:
            seen[num] = idx

numbers =[2,7,3,6]
target_val = 9
result = two_sum(numbers,target_val)


if result:
    print("Result Indices:", result)
    print(f"Values: {numbers[result[0]]} + {numbers[result[1]]} = {target_val}")
else:
    print("No valid pair found that sums to target.")


