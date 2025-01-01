# @param {String[]} words
# @param {Character} x
# @return {Integer[]}
def find_words_containing(words, x)
res=[]
for i in 0...words.length
     for j in 0...words[i].length
        if words[i][j]==x
         res<<i
         break
        end
    end 
 end 
    res
end