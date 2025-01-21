# @param {String} s
# @return {String}
def frequency_sort(s)
  freq = Hash.new(0)
  s.each_char { |char| freq[char] += 1 }

  # Step 2: Sort characters by frequency in descending order
  sorted = freq.sort_by { |char, count| -count }.flat_map { |char, count| [char] * count }

  # Step 3: Convert the sorted array back to a string
  sorted.join

end