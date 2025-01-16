# @param {Integer[]} arr1
# @param {Integer[]} arr2
# @return {Integer[]}
def relative_sort_array(arr1, arr2)
     # Create a hash to store the frequency of elements in arr1
  freq_map = Hash.new(0)
  
  # Count occurrences of elements in arr1
  arr1.each { |num| freq_map[num] += 1 }
  
  # Initialize result array to store the final result
  result = []

  # Add elements from arr2 to result in the same order as arr2
  arr2.each do |num|
    freq_map[num].times { result << num }
  end
  
  # Add remaining elements that are not in arr2, sorted in ascending order
  remaining = freq_map.keys.reject { |num| arr2.include?(num) }.sort
  remaining.each do |num|
    freq_map[num].times { result << num }
  end
  
  result
end