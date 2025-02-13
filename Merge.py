def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined

def merge_sort(mainList):
    if len(mainList) == 1:
        return mainList
    mid_index = int(len(mainList)/ 2)
    left = merge_sort(mainList[:mid_index])
    right = merge_sort(mainList[mid_index:])
    return merge(left, right)

list1 = [3,4,5,7,50]
list2 = [1,67,68,3,7,756,32,84]

print(merge_sort(list2))