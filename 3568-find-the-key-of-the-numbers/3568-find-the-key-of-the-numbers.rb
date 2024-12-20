# @param {Integer} num1
# @param {Integer} num2
# @param {Integer} num3
# @return {Integer}
def generate_key(num1, num2, num3)
      num1=num1.to_s.rjust(4,"0")
    num2=num2.to_s.rjust(4,"0")
    num3=num3.to_s.rjust(4,"0") 
    res=""
    for i in 0...num3.length
        res+=[num1[i].to_i,num2[i].to_i,num3[i].to_i].min.to_s
    end
    return res.to_i.abs 
end