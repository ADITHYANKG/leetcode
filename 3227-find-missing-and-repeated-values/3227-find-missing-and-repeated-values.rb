# @param {Integer[][]} grid
# @return {Integer[]}
def find_missing_and_repeated_values(grid)
      # Flatten the 2D grid into a 1D array
  flat_list = grid.flatten

  # Create a hash to count occurrences
  counts = Hash.new(0)
  flat_list.each { |num| counts[num] += 1 }

  # Initialize variables for the repeated and missing numbers
  repeated = nil
  missing = nil

  # Determine the range of numbers
  n = grid.size
  (1..n * n).each do |num|
    if counts[num] == 2
      repeated = num
    elsif counts[num] == 0
      missing = num
    end
  end

  # Return the result
  [repeated, missing]

end