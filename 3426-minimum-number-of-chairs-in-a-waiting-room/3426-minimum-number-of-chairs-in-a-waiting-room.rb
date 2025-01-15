# @param {String} s
# @return {Integer}
def minimum_chairs(s)
 current_chairs = 0
  max_chairs = 0

  s.each_char do |event|
    if event == 'E'
      current_chairs += 1
    elsif event == 'L'
      current_chairs -= 1
    end
    max_chairs = [max_chairs, current_chairs].max
  end

  max_chairs
   
    
end