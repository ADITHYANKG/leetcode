# @param {String} s
# @return {String}
def sort_sentence(s)
arr=[]
    s.split.each do |word|
      arr[word[-1].to_i]=word[0...word.length-1]
    end
    arr.join(" ").strip  
end