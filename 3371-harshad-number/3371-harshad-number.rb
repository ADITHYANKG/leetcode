# @param {Integer} x
# @return {Integer}
def sum_of_the_digits_of_harshad_number(x)
    s=0
    y=x
    while x>0
      s+=x%10
      x=x/10
   end 
   if y%s==0
     return s
   end
   return -1     
end