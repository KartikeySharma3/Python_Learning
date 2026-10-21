def find_duplicate_element(num):

    duplicates = []

    for i in range(1, len(num)):

        if num[i] == num[i-1]:

            if not duplicates or duplicates[-1] != num[i]:

                duplicates.append(num[i])

    return duplicates 


sorted_number =[1,2,2,3,3,4,6,9]

result = find_duplicate_element(sorted_number)
print(f"Duplicate numbers: {result}")           
