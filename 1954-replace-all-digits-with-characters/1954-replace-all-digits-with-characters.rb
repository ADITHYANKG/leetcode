# @param {String} s
# @return {String}
def replace_digits(s)
res=""
   for i in 0...s.length
      if i%2==0
        res+=s[i]
      else
        c=(s[i-1].ord+s[i].to_i).chr
        res+=c
     end
  end
  res      
      
    
end