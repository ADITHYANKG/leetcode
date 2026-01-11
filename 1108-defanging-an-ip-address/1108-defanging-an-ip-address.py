class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        out=""
        for i in range(len(address)):
            if address[i]==".":
                out+="[.]"
            else:
                out+=address[i]

        return out      
        