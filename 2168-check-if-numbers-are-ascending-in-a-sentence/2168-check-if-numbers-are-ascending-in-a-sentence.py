class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        a=s.split()
        res=[]
        for i in range(len(a)):
            if a[i].isnumeric():
                res.append(a[i])

        for i in range(len(res)-1):
            if int(res[i])>=int(res[i+1]):
                    return False

            
        return True

