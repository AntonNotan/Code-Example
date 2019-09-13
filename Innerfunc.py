def Merge(A,p,q,r):
    B=[]

    if A[r-1]<=A[p-1]:
        B = A[:]
        if (p + r) % 2 != 0:
            for i in range(q, r):
                A[p + i - q - 1] = B[i]
            for i in range(p - 1, q):
                A[i + (q - (p - 1))] = B[i]
        else:
            for i in range(q, r):
                A[p + i - q - 1] = B[i]
            for i in range(p - 1, q):
                A[i + (q - (p))] = B[i]

    elif A[q]<A[q-1]:
        j=p-1
        for i in range(q, r):
            if j < i:
                while (A[j] <= A[i]) and (j < i):
                     j += 1
                if j == i:
                    break
                Q = A[j]
                A[j] = A[i]
                if (i - j) > 1:
                    for k in range(1, i - j):
                        A[i + 1 - k] = A[i - k]
                j += 1
                A[j] = Q
        return A
