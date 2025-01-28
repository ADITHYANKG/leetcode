# @param {Integer[]} nums
# @return {Integer}
def subarray_sum(nums)
    sum=0
    for i in 0...nums.length
       start=[0,i-nums[i]].max
       sum+=nums[start..i].sum
    end
    sum 
end