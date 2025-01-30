# @param {Integer[]} nums
# @return {Integer[]}
def running_sum(nums)
    out=[]
     for i in 0...nums.length
         out<< nums[0..i].sum
     end
     out    
end