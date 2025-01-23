# @param {Integer[]} nums
# @return {Integer}
def max_adjacent_distance(nums)
res=[]
 for i in  0...nums.length-1
     d=nums[i+1]-nums[i]
     res<<d.abs
  end
  l=nums[-1]-nums[0]
  res<<l.abs
  res.max 
end