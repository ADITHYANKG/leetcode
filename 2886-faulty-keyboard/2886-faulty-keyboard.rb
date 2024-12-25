# @param {String} s
# @return {String}
def final_string(s)
   s=s.split("")
    res=[]
    for x in s
    if x=='i'
    res=res.reverse
    else res.push(x)
    end
    end
 return res.join("")


end