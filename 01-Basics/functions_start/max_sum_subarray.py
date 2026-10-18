"""
Problem: Maximum Sum Subarray of Size K
Pattern: Fixed-Size Sliding Window
Time Complexity: O(N) — Single pass after the initial window of size k
Space Complexity: O(1) — No auxiliary data structures allocated
"""

def max_sum_subarray(nums: list[int], k: int) -> int:
    n = len(nums)

    if n < k or k <= 0:
        return 0

    window_sum = sum(nums[:k])
    max_sum = window_sum 

    for i in range(k, n):
       
        window_sum += nums[i] - nums[i - k]
        
        # Track the peak sum encountered
        if window_sum > max_sum:
            max_sum = window_sum

    return max_sum

if __name__ == "__main__":
    test_arr = [1, 7, 2, 8, 4, 3]
    k_val = 3
    result = max_sum_subarray(test_arr, k_val)
    print(f"Array: {test_arr}, k = {k_val}")
    print(f"Maximum Contiguous Subarray Sum: {result}") 


        