def binary_search_recursive(elements,begin,end,x):
    if begin is end:
        return elements[begin] is x
    center = ((end - begin)// 2) + begin

    if x < elements [center]:
        return binary_search_recursive(elements,begin,center,x)
    elif x > elements [center]:
        return binary_search_recursive(elements,center + 1,end,x)
    return True

def binary_search(elements,x):
    if elements is None or len(elements) == 0:
        return False
    return binary_search_recursive(elements,0,len(elements)-1,x)

print(binary_search([1,2,3,5],1))
print(binary_search([1,2,3,5],7))