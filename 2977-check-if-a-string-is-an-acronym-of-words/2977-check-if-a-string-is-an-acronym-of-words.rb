# @param {String[]} words
# @param {String} s
# @return {Boolean}
def is_acronym(words, s)
  res=""
   words.each do |w|
     res+=w[0]
   end
   
  if res==s
     true
 else 
   false
   end       
        
    
end