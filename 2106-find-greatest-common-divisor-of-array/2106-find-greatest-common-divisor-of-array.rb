# @param {Integer[]} nums
# @return {Integer}
def find_gcd(nums)
    nums=nums.sort
    res=0
    n=nums[-1]
    while n>=1
    if nums[0]%n==0 and nums[-1]%n==0
           res=n
           break
      end
      n=n-1
      end
      return res



end