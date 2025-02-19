# @param {String[]} words
# @return {Integer}
def maximum_number_of_string_pairs(words)
c=0
for i in 0...words.length-1
   for j in i+1...words.length
   if words[i]==words[j].reverse
      c+=1
   end
   end
   end
   c   
    
end