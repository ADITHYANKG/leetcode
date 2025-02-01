# @param {String} word
# @return {Integer}
def num_different_integers(word)
arr=[]
i=0
    while i< word.length
        
     if word[i].ord<=57
       w=word[i]
       
       for j in i+1...word.length
          if word[j].ord<=57
          w+=word[j]
          m=j
          else
          break
          end
       end
       arr <<w.to_i
       i+=w.length
       
    else
     i+=1
     end

    end    
   arr.uniq.length        
end