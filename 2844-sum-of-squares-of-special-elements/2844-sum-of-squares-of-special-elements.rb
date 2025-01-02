# @param {Integer[]} nums
# @return {Integer}
def sum_of_squares(nums)
   sum=0
   nums.each_with_index do |num,i|
      if nums.length% (i+1)==0
        sum+=(num**2)
      end 
   end

    sum
end