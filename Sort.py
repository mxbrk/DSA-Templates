def bubble_sort(mainList):
    for i in range(len(mainList) -1, 0, -1):
        for j in range(i):
            if mainList[j] > mainList[j+1]:
                temp = mainList[j]
                mainList[j] = mainList[j+1]
                mainList[j+1] = temp
    return mainList

def selected_sort(mainList):
    for i in range(len(mainList) -1):
        min_index = i
        for j in range(i+1, len(mainList)):
            if mainList[j] < mainList[min_index]:
                min_index = j
        if i != min_index:        
            temp = mainList[i]
            mainList[i] = mainList[min_index]
            mainList[min_index] = temp
    return mainList

def insertion_sort(mainList):
    for i in range(1,len(mainList)):
        temp = mainList[i]
        j = i-1
        while temp < mainList[j] and j > -1:
            mainList[j+1] = mainList[j]
            mainList[j] = temp
            j -=1
    return mainList