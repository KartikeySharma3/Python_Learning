def max_sum_subarray(nums,k):
    n = len(nums)

    if n<k and k<=0:
        return 0

    window_sum = sum(nums[:k])
    max_sum= window_sum 

    for i in range(k,n):
        window_sum += nums[i] - nums[i-k]

        if window_sum > max_sum:
            max_sum = window_sum

    return max_sum

if __name__ == "main":
    test_arr =[10,8,9,6,3,7]
    k_val =3
    result =max_sum_subarray(test_arr,k_val)
    print(f"Array: {test_arr}, k:{k_val}")
    print(f"the result is{result}")


