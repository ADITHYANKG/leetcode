# @param {String} sentence
# @param {String} search_word
# @return {Integer}
def is_prefix_of_word(sentence, search_word)
    arr=sentence.split
    l=search_word.length
    for i in 0...arr.length
       if arr[i][0...l]==search_word
          return i+1
          break
       end
    end
    return -1      
end