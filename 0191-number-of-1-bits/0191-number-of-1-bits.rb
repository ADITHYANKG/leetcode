# @param {Integer} n
# @return {Integer}
def hamming_weight(n)
count=0
    while n>0
     if n%2!=0
       count+=1
      end
     n=n/2.to_i
    end
    count 

end