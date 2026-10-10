def find_unique_element(num):
    uniques = []
    for i in range(0, len(num)):
        
            
        if num[i] != num[i-1]:
            if not uniques or uniques[-1] != num[i]:
                uniques.append(num[i])
    return uniques 
sorted_number =[1,2,2,3,3,4,6,9]
result = find_unique_element(sorted_number)
print(f"Duplicate numbers: {result}")           
