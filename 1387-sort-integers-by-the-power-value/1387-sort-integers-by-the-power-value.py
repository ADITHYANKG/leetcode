class Solution(object):
    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        p=[]
        for n in range(lo,hi+1):
            org=n
            step=0
            while n>1:
                if n%2==0:
                    n=n/2
                else:
                    n=3*n+1    
                step+=1
            p.append(step)    
        li=list(range(lo,hi+1)) 
        for i in range(len(p)):
            for j in range(len(p)-1):
                if p[j]>p[j+1]:
                    p[j],p[j+1]=p[j+1],p[j]
                    li[j],li[j+1]=li[j+1],li[j]
        return li[k-1]         