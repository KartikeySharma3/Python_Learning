def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue
        
        if s[left].lower() != s[right].lower():
            return False
            
        left += 1
        right -= 1
    print("Result: True (Valid Palindrome)")
    return True
text1 = "A man, a plan, a canal: Panama"
text2 = "race a car"

is_palindrome(text1)
is_palindrome(text2)