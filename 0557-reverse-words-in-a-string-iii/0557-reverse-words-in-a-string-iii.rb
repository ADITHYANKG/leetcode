# @param {String} s
# @return {String}
def reverse_words(s)
   res=""
    s.split.each do |w|
      res+=w.reverse+" "
     end
     res.rstrip

end