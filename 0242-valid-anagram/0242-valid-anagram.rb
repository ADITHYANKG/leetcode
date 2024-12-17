# @param {String} s
# @param {String} t
# @return {Boolean}
def is_anagram(s, t)
  a=s.split("").sort
  b=t.split("").sort
  if a==b
  return true
  else 
  false
  end
    
end