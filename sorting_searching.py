# 1. Binary Search
listdata = [5,7,9,10,15,19,20,25,26,29,35,36,38]
element = 26
start = 0
end = len(listdata) - 1
while True:
    m = (start + end) // 2
    if element == listdata[m]:
        print('element found at position', m)
        break
    elif element < listdata[m]:
        end = m
    else:
        start = m
    if end - start == 1:
        print('element not found')
        break

# 2. Merge sort
listdata = [11,28,6,1,2,9,75,12,46,20,15,13,17,6,5,3]


def mergesort(listdata):
    if len(listdata) > 1:
        m = len(listdata) // 2
        start = listdata[:m]
        R = listdata[m:]
        mergesort(start)
        mergesort(R)
        i = j = k = 0
        while i < len(start) and j < len(R):
            if start[i] < R[j]:
                listdata[k] = start[i]
                i += 1
            else:
                listdata[k] = R[j]
                j += 1
            k += 1

        while i < len(start):
            listdata[k] = start[i]
            i += 1
            k += 1

        while j < len(R):
            listdata[k] = R[j]
            j += 1
            k += 1


mergesort(listdata)
print(listdata)


# 3. quick sort

def partition(start, end, listdata):
    pi = start
    pv = listdata[pi]
    while start < end:
        while start < len(listdata) and listdata[start] <= pv:
            start += 1
        while listdata[end] > pv:
            end -= 1
        if start < end:
            listdata[start], listdata[end] = listdata[end], listdata[start]
    listdata[end], listdata[pi] = listdata[pi], listdata[end]
    return end


def quicksort(start, end, listdata):
    if start < end:
        p = partition(start, end, listdata)
        quicksort(0, p - 1, listdata)
        quicksort(p + 1, end, listdata)


listdata = [11,28,6,1,2,9,75,12,46,20,15,13,17,6,5,3]
quicksort(0, len(listdata) - 1, listdata)
print(listdata)


# 4. Isertion sort

def insertionsort(listdata):
    for i in range(1, len(listdata)):
        if listdata[i - 1] > listdata[i]:
            val = listdata[i]
            j = i - 1
            while j >= 0 and val < listdata[j]:
                listdata[j + 1] = listdata[j]
                j -= 1
            listdata[j + 1] = val


listdata = [11,28,6,1,2,9,75,12,46,20,15,13,17,6,5,3]
insertionsort(listdata)
print(listdata)

# 5. Sort strings
listdata = ['bunny', 'chintu', 'sai kumar', 'chotu', 'zebra', 'apple', 'banana']
quicksort(0, len(listdata) - 1, listdata)
print(listdata)
