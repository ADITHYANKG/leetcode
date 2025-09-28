class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        stack=[]
        k=0
        res=[]
        i=1
        while target!=stack and  i<=n:
              stack.append(i)
              res.append("Push")
              if stack[-1]!=target[k]:
                res.append("Pop")
                stack.pop()
              i+=1   
              if stack and stack[-1]==target[k]:
                k+=1
        return res       
                

                  

            


              
        