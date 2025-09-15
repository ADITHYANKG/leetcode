class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.capacity=maxSize
        self.arr=[0]*self.capacity
        self.top=-1
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.top==self.capacity-1:
            return
        self.top+=1
        self.arr[self.top]=x



        

    def pop(self):
        """
        :rtype: int
        """
        if self.top==-1:
            return -1
        val=self.arr[self.top]
        self.top-=1
        return val


 

        
        

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        if k>self.top:
            for i in range(0,self.top+1):
                self.arr[i]=self.arr[i]+val
        else:
            for i in range(0,k):
                self.arr[i]=self.arr[i]+val       

        

        

        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)