def insertSort(A):
    if len(A) <2:
        return A
    result = [0 for i in xrange(len(A))]
    result[0] = A[0]
    for i in xrange(1,len(A)):
        for j in xrange(i-1,-1,-1):
            if A[i] < result[j]:
                result[j+1] = result[j]
            else:
                result[j+1] = A[i]
                break
    return result

if __name__ == "__main__":
    #test
    a= [1,3,5,2,7,9,4,6,8]
    print insertSort(a)
