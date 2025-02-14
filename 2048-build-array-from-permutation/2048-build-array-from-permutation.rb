# @param {Integer[]} nums
# @return {Integer[]}
def build_array(nums)
    ans=[]
    for i in 0...nums.length
        ans<<nums[nums[i]]
     end
     ans   
end