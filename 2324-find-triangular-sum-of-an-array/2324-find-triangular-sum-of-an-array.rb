# @param {Integer[]} nums
# @return {Integer}
def triangular_sum(nums)
     res=nums
    while nums.length>1
        res=[]
      for i in 0...nums.length-1
         res << (nums[i]+nums[i+1])%10
      end
      nums=res
    end
    nums[0]   
end