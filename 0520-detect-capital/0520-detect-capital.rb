# @param {String} word
# @return {Boolean}
def detect_capital_use(word)
    stat=true
    if word.upcase==word
    return stat
    end
   for i in 1...word.length
       if word[i]!=word[i].downcase
            stat=false
            break
        end
    end    
    return stat
    
end