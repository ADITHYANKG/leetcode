# @param {String} s
# @return {String}
def reverse_only_letters(s)
    a=""
    for i in 0...s.length
        if (s[i].ord>=65 and s[i].ord<=90) or (s[i].ord>=97 and s[i].ord<=122)
          a+=s[i]
        end 
    end

    l=a.length-1
    res=""
    k=0
    for i in 0...s.length
       if (s[i].ord>=65 and s[i].ord<=90) or (s[i].ord>=97 and s[i].ord<=122)
          res+=a[l-k]
          k+=1
       else
          res+=s[i]
       end
    end
    res
end