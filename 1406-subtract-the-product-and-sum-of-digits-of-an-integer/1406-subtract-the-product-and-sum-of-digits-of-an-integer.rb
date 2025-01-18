# @param {Integer} n
# @return {Integer}
def subtract_product_and_sum(n)
s=0
p=1
   while n>0
    d=n%10
    s=s+d
    p=p*d
    n=n/10
   end
   p-s
end