# @param {String[]} words
# @return {String}
def odd_string(words)
    difference_arrays = words.map do |word|
    (0...word.length - 1).map { |i| word[i + 1].ord - word[i].ord }
  end

  # Step 2: Identify the unique difference array
  # Count occurrences of each difference array
  counts = Hash.new(0)
  difference_arrays.each { |diff_array| counts[diff_array] += 1 }

  # Find the unique difference array (appears only once)
  unique_diff = counts.key(1)

  # Step 3: Find and return the corresponding word
  words[difference_arrays.index(unique_diff)]


        
end