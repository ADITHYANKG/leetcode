# @param {Integer[]} nums
# @return {Float}
def minimum_average(nums)
 nums.sort!
  
  # Initialize averages array
  averages = []

  # Iterate while pairing smallest and largest
  while nums.length > 1
    min_element = nums.shift  # Remove smallest element
    max_element = nums.pop    # Remove largest element
    average = (min_element + max_element) / 2.0
    averages << average       # Add to averages
  end

  # Return the smallest average
  averages.min 
    
end