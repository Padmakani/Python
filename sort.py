
def binarys(array, num, minlen, maxlen):
    key = (minlen+maxlen)/2
    if num == array[key]:
        return key
    elif num<array[key]:
        return binarys(array, num, minlen, key-1)
    elif num>array[key]:
        return binarys(array, num, minlen+1, key)
    else:
        return NOT_FOUND

A =[3,4,5,6] 

result = binarys(A, 5, 1, len(A))

print result
