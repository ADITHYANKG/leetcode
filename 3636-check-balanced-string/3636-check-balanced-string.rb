# @param {String} num
# @return {Boolean}
def is_balanced(num)
    eve=0
    odd=0
    for i in 0...num.length
        if i%2==0
         eve+=num[i].to_i
        else
        odd+=num[i].to_i
        end
    end
    if eve==odd
     return true
    else
    return false
    end

end