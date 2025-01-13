# @param {Integer[]} nums
# @return {Integer}
def max_product(nums)
   nums=nums.sort
   max1=nums[-1]-1
   max2=nums[-2]-1
   max1*max2
    
end