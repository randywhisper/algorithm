def quickSort(A,m,n):
    if n >m:
        q = mergeStep(A,m,n)
        quickSort(A,m,q-1)
        quickSort(A,q+1,n)
def mergeStep(a,m,n):
    p = m
    for i in xrange(m,n+1):
        if a[i] <a[n]:
            a[i],a[p] = (a[p],a[i])
            p+=1
    a[n],a[p] = (a[p],a[n])
    return p

if __name__ == "__main__":
    #test
    a = [8,7,1,6,9,2,3,5,4]
    quickSort(a,0,8)
    print a

