def sum_three(nums):
    nums.sort()
    triplets = []
    n = len(nums)

    for i in range(n-2):
        if nums[i] >0:
           break

        if i >0 and nums[i] == nums[i-1]:
            continue

        left = i+1
        right = n-1

        while left < right :
            current_sum = nums[i] +nums[right] + nums[left]

            if current_sum <0:
                left +=1
            elif current_sum>0:
                right -=1
            else:
                triplets.append([nums[i],nums[right],nums[left]])

                while left < right and nums[left] == nums[left+1]:
                    left +=1
                while left < right and nums[right] == nums[right-1]:
                    right -=1
                left +=1
                right -=1
    return triplets

if __name__ == "__main__":                        
    sample_sum = [-1,0,1,2,-1,4]
    result =sum_three(sample_sum)
    print(f"Input array: {sample_sum}")
    print(f"Unique 3 Sum: {result} ")