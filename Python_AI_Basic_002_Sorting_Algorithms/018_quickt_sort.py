def quicksort(l):
    def quicksort_recursive(l,i,j):
        if i < j:
            k = partition(l,i,j)
            quicksort_recursive(l,i,k-1)
            quicksort_recursive(l,k+1,j)
    quicksort_recursive(l,0,len(l)-1)

def partition(l,i,j):
    x = l[j]
    k = i - 1
    for h in range(i,j):
        if l[h] <= x:
            k += 1
            temp = l[h]
            l[h] = l[k]
            l[k] = temp
    temp = l[k+1]
    l[k+1] = l[j]
    l[j] = temp
    return k + 1

l = [2,3,5,1,3,5,3,6,7,3,9]
quicksort(l)
print(l)
