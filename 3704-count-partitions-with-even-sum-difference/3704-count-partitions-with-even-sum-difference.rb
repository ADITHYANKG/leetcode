# @param {Integer[]} nums
# @return {Integer}
def count_partitions(nums)
c=0
    for i in 1...nums.length
       if (nums[0...i].sum-nums[i...nums.length].sum)%2==0
            c+=1

       end
    end
    c   
         
end