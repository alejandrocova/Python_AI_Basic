def max_heapify(l,i,size):
    left = 2 * i + 1
    right = 2 * i + 2
    if left < size and l[left] > l[i]:
        maximum = left
    else:
        maximum = i

    if right < size and l[right] > l[maximum]:
        maximum = right
    if maximum is not i:
        temp = l[i]
        l[i] = l[maximum]
        l[maximum] = temp
        max_heapify(l,maximum,size)

def heap_build(l):
    heap_size = len(l)
    for i in range(int(len(l)/2),-1,-1):
        max_heapify(l,i,heap_size)

def heap_sort(l):
    heap_build(l)
    heap_size = len(l)
    for i in range(len(l), 0, -1):
        temp = l[0]
        l[0] = l[i]
        l[i] = temp
        heap_size -= 1
        max_heapify(l,1,heap_size)


l = [3,5,2,1]
heap_sort(l)
print(l)