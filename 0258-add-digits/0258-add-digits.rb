# @param {Integer} num
# @return {Integer}
def add_digits(num)
     num=num.to_s
      res=num.to_i
      p res
      while res.to_s.length>1
        temp=0
        for i in 0...res.to_s.length
            temp+=res.to_s[i].to_i
         end
         res=temp
         p temp   
          
      end

      
          res
end