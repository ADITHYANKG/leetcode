# @param {Integer[]} nums
# @return {Integer[]}
def sorted_squares(nums)
    nums=nums.map{
        |n|
        n*n
        
    }
   nums.sort
end