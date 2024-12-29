# @param {Integer} n
# @return {Integer}
def sum_of_multiples(n)
res=0
for i in 1..n
if i%3==0  or i%5==0 or i%7==0
     res+=i
    end
    end
    res
end