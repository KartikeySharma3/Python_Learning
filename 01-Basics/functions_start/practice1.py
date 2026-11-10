def is_palindrone(s):
    left =0
    right =0
    j  = len(s)
    while left <right:
        if not s[left].isalnum():
            left +=1
            continue
        if not s[right].isalnum():
            right -=1
            continue
        if s[left].lower() != s[right].lower():
            return False
            
        left +=1
        right -=1
    print("Result: (valid palindrone)")
    return True
        


text1 = "A man, a plan, a canal: Panama"
text2 = "race a car"

is_palindrone(text1)
is_palindrone(text2)
