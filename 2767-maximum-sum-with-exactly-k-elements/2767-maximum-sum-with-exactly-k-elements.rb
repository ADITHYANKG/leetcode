# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def maximize_sum(nums, k)
res=[]
for i in 0...nums.length
sum=0
   for j in 0...k
      sum+=nums[i]
      nums[i]+=1
   end
   res<<sum
 end
 res.max     
      
    
end