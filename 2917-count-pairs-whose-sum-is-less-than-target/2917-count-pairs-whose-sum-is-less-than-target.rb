# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def count_pairs(nums, target)
      c=0
    for i in 0...nums.length-1
      for j in (i+1)...nums.length
           if (nums[i]+nums[j])<target
               c+=1
           end
      end
    end
    c           

         
end