# @param {Integer[]} nums
# @return {Integer}
def majority_element(nums)
    frequency = Hash.new(0)
  big = 0
  bign = nil

 
  nums.each do |num|
    frequency[num] += 1
    
    if frequency[num] > big
      big = frequency[num]
      bign = num
    end
  end

  bign
end