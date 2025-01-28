# @param {Integer[]} nums
# @return {Boolean}
def can_alice_win(nums)
     a1=nums.select{ |x| x%10==x}
     b1=nums.select{|x| x%10!=x}
     a2=nums.select{ |x| x%10!=x}
     b2=nums.select{|x| x%10==x}
     if a1.sum>b1.sum or a2.sum>b2.sum
      return true
     end
     false
end