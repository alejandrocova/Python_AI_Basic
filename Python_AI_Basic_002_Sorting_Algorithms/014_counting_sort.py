def countingsort(l,k):
    result = [0] * (len(l))
    c = [0] * (k+1)
    same_number_elements_i(l,c)
    less_number_elements_i(c)
    for i in range(len(l)-1, -1,-1):
        c[l[i]] -= 1
        result[c[l[i]]] = l[i]
    return result

def same_number_elements_i(l,c):
    for i in range(len(l)):
        c[l[i]] += 1

def less_number_elements_i(c):
    for i in range(1,len(c)):
        c[i] = c[i] +c[i-1]