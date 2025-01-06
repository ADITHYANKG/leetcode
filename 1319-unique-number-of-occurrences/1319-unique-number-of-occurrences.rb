# @param {Integer[]} arr
# @return {Boolean}
def unique_occurrences(arr)
  freq = Hash.new(0)
  arr.each { |num| freq[num] += 1 }

  # Step 2: Check if frequencies are unique
  occurrences = freq.values
  occurrences.uniq.size == occurrences.size  
end