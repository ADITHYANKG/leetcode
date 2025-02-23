# @param {Integer[]} nums
# @return {Integer}
def find_max_k(nums)
while nums.length>1
   if nums.include?(-nums.max)
    return nums.max  
   end
  nums.delete(nums.max)
end
  -1
end