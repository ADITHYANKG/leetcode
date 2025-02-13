# @param {Integer[]} nums
# @return {Integer}
def find_non_min_or_max(nums)
    n=nums.sort
    if n.length>2
     return n[1]
    else
    return -1
    end  
end