class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def is_numeric(s):
            try:
                float(s)
                return True
            except ValueError:
                return False
              
        op=[]
        n=[]
        result=[]
        
        for i in range(len(tokens)):
            # print("result",result)
            if is_numeric(tokens[i]):
                n.append(int(tokens[i]))
                result.append(int(tokens[i]))
            else:
                n1=result.pop()
                n2=result.pop()
                # print("operation",tokens[i])
                if tokens[i]=="+":
                    result.append(n2+n1)
                if tokens[i]=="-":
                    result.append(n2-n1)
                if tokens[i]=="*":
                    result.append(n2*n1)
                if tokens[i]=="/":
                    result.append(int(n2/n1))
                    
                
        return result[0]         