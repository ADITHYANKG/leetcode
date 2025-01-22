# @param {String} s
# @return {String}

def greatest_letter(s)
  seen = Set.new
  result = ""

  s.each_char do |char|
    if char == char.downcase && seen.include?(char.upcase) ||
       char == char.upcase && seen.include?(char.downcase)
      result = [result, char.upcase].max
    end
    seen.add(char)
  end

  result   
    
end
