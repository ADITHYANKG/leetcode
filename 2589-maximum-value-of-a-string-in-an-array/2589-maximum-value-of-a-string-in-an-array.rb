# @param {String[]} strs
# @return {Integer}
def maximum_value(strs)
   res=strs.map{|a| 
   if a.match?(/\A-?\d+\z/)
     a.to_i
    else
      a.length 
     end 
   }
   return res.max
end