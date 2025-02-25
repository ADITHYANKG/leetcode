# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def sum_of_good_numbers(nums, k)
       s=0
    for i in 0...nums.length
    puts "#{i-k},#{i+k}"
    puts  "nums=#{nums[i]},#{nums[i-k]}"
    if i-k>=0 and i+k<nums.length
            if  nums[i]>nums[i-k] and nums[i]>nums[i+k] 
                puts nums[i]
            s+=nums[i]
            end
     elsif i-k<0 and i+k<nums.length
         if nums[i]>nums[i+k]
         puts nums[i]
         s+=nums[i]
         end
 elsif i-k>=0 and i+k>=nums.length
     if nums[i]>nums[i-k]
         puts nums[i]
         s+=nums[i]
        end
     end
     end
     s   
        
end