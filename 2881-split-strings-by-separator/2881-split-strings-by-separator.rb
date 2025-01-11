# @param {String[]} words
# @param {Character} separator
# @return {String[]}
def split_words_by_separator(words, separator)
   res=[]
    words.each do |word|
     res.concat(word.split(separator))
    end
    res.reject(&:empty?)
end