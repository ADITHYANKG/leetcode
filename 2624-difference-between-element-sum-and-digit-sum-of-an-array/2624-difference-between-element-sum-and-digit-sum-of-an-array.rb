# @param {Integer[]} nums
# @return {Integer}
def difference_of_sum(nums)
   e=nums.sum
   d=0
   for i in 0...nums.length
        if nums[i]>=10
            g=nums[i]
             while g>0
                  d+=g%10
                  g/=10
             end
        else
           d+=nums[i]
        end   
    end
       (e-d).abs              
end