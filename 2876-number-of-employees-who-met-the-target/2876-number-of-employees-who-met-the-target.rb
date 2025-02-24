# @param {Integer[]} hours
# @param {Integer} target
# @return {Integer}
def number_of_employees_who_met_target(hours, target)
   res=0
    hours.each do |n|
     if n>=target
     res+=1
     end
     end
     res

end