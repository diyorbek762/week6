def merge_sorted_lists(list1, list2):
    j=0
    i=0
    merged=[]
    result_list=[]
    while i<len(list1) and j<len(list2):
        if list1[i]>list2[j]:
            merged.append(list2[j])
            j+=1
        elif list1[i]<list2[j]:
            merged.append(list1[i])
            i+=1
        elif list1[i] == list2[j]:
            merged.append(list1[i])
            merged.append(list2[j])
            i+=1
            j+=1
    while i<len(list1):
        merged.append(list1[i])
        i+=1
    while j<len(list2):
        merged.append(list2[j])
        j+=1
    
    return merged


print(merge_sorted_lists(list1 = [3, 7, 11],
list2 = [2, 5, 9, 12]))
# Case 1: Standard case
l1 = [1, 5, 9, 10]
l2 = [2, 3, 8]
# Expected Output: [1, 2, 3, 5, 8, 9, 10]
print(merge_sorted_lists(l1, l2))
# Case 2: One list is empty
l3 = []
l4 = [4, 6, 7]
# Expected Output: [4, 6, 7]
print(merge_sorted_lists(l3, l4))
# Case 3: Lists with different lengths
l5 = [10, 20, 30, 40, 50]
l6 = [15, 25]
# Expected Output: [10, 15, 20, 25, 30, 40, 50]
print(merge_sorted_lists(l5, l6))
# Case 4: Both lists are empty
l7 = []
l8 = []
# Expected Output: []
print(merge_sorted_lists(l7, l8))