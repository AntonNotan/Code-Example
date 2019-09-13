from Innerfunc import Merge

def Sort(A,p,r):
    if p<r:
        q=round((p+r)/2-0.01)
        print(p,q)
        Sort(A,p,q)
        print(q+1,r)
        Sort(A,q+1,r)
         Merge(A,p,q,r)
        return A
