# @param {Integer} low
# @param {Integer} high
# @return {Integer}
def count_symmetric_integers(low, high)
    def dig(n)
    n=n.to_i
    res=[]
    while n>0
     d=n%10
     res<< d
     n=n/10
    end
     res

    end
      
    
    c=0
    for i in low..high
    l=i.to_s.length
     if dig(i.to_s[0...l/2]).sum==dig(i.to_s[l/2...l]).sum and l%2==0
     c+=1
     end
     end
     c

end