class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        p=int((len(arr)/100)*5)
        temp=arr[p:len(arr)-p]
        return sum(temp)/len(temp)