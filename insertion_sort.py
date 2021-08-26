import math
from random import randrange

upper_range = 100
lower_range = 0
list_length = 20

list = []
for i in range(list_length):
    list.append(randrange(lower_range, upper_range))

#list = [7,3,2,4]
print('Unsorted List', list)

def insertion_sort(list):
    for i, element in enumerate(list):
        print("Current:", list[i])
        j = i-1
        print("MAIN i:", i, "j:", j)
        for e in range(i):
            if j>=0 and list[j]>list[i]:
                list[j], list[i] = list[i], list[j]
                print("SUB i:", i, list)
                i=i-1
                j=j-1
            
    return list

print('Sorted List:', insertion_sort(list))