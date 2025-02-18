# @param {Integer[]} nums
# @return {Integer[]}
def separate_digits(nums)
    res=[]
    for i in 0...nums.length
       if nums[i]<10
           res<<(nums[i])
       else
          temp=[]
          while nums[i]>0
              temp.unshift(nums[i]%10)
              nums[i]=nums[i]/10
          end
          res<<temp
       end
     end         

              


     res.flatten

end