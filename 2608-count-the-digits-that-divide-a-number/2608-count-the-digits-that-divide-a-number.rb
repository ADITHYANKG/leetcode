# @param {Integer} num
# @return {Integer}
def count_digits(num)
temp=num
c=0
    while num>0
     d=num%10
     if temp%d==0
       c+=1
     end
     num=num/10
     end
     c  


end