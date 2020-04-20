myList = []

def quick_sort(myList):
    if len(myList) <= 1 :
        return myList
    pivot = myList[len(myList) // 2]
    less_list, equal_list, big_list = [], [], []

    for i in myList:
        if i < pivot:
            less_list.append(i)
        elif i > pivot:
            big_list.append(i)
        else:
            equal_list.append(i)

    return quick_sort(less_list) + equal_list + quick_sort(big_list)

myList = list(map(int, input("Input: ").split() ))

print("Output:",quick_sort(myList))
