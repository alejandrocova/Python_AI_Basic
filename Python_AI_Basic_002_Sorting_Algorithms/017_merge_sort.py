def merge_sort(l):
    def merge_sort_recursive(l,i,j):
        if i < j:
            k = int((i+j)/2)
            merge_sort_recursive(l,i,k)
            merge_sort_recursive(l,k+1,j)
            mix(l,i,k,j)
    merge_sort_recursive(l,0,len(l) - 1)

def mix(l,i,k,j):
    len_sublist_left = k - i + 1
    len_sublist_right = j - k
    left = []
    right = []
    for h in range(len_sublist_left):
        left.append(l[i+h])
    for h in range(len_sublist_right):
        right.append(l[k+h+1])
    i1 = 0
    i2 = 0
    for h in range(i,j+1):
        if i1 < 0:
            l[h] = right[i2]
            i2 += 1
        elif i2 < 0:
            l[h] = left[i1]
            i1 += 1
        elif left[i1] <= right[i2]:
            l[h] = left[i1]
            i1 += 1
            if i1 >= len(left):
                i1 = -1
        else:
            l[h] = right[i2]
            i2 += 1
            if i2 >= len(right):
                i2 = -1

l = [2,4,1,3,5,4,5,0,5,8,3,2,9]
merge_sort(l)
print(l)