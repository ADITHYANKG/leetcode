class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        op=['(','[','{']
        cl=[')',']','}']
        for i in range(len(s)):
            if s[i] in op:
                stack.append(s[i])
            if s[i] in cl:
                if stack and (op.index(stack[-1])==cl.index(s[i])):
                    stack.pop()
                else:
                    return False    
        if len(stack)==0:
            return True
        else:
            return False                




        