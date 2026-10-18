"""
Problem: Longest Substring Without Repeating Characters
Pattern: Dynamic Sliding Window with Hash Map (Index Lookup)
Time Complexity: O(N) — Each character is inspected once; left pointer only jumps forward
Space Complexity: O(min(N, M)) — Dictionary stores unique characters in the window
"""

def longest_substring_without_repeating(s: str) -> tuple[int, str]:
    char_index_map = {}  # Stores character -> last seen index
    left = 0
    max_len = 0
    start_idx = 0 

    for right, char in enumerate(s):
        # If the character was seen inside the current window, jump 'left' past it
        if char in char_index_map and char_index_map[char] >= left:
            left = char_index_map[char] + 1

        char_index_map[char] = right

        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len
            start_idx = left

    longest_str = s[start_idx : start_idx + max_len]
    return max_len, longest_str

if __name__ == "__main__":
    test_str = "asdfghjytreteqaxzvvagh"
    length, substr = longest_substring_without_repeating(test_str)
    print(f"Input: '{test_str}'")
    print(f"Max Length: {length}")
    print(f"Longest Substring: '{substr}'")