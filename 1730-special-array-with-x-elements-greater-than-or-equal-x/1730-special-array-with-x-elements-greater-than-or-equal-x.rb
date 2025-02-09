# @param {Integer[]} nums
# @return {Integer}
def special_array(nums)
    for i in 0..nums.length
      c=0
        for j in 0...nums.length
          if nums[j]>=i
          c+=1
          end
        end
        if c==i
           return i
        break
        end
    end          

return -1
       

    
end