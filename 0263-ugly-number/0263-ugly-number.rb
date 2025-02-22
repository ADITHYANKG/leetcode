# @param {Integer} n
# @return {Boolean}

def is_ugly(n)
  return false if n <= 0  # Ugly numbers must be positive

  # Check divisibility by 2, 3, and 5 only
  [2, 3, 5].each do |factor|
    while n % factor == 0
      n /= factor
    end
  end

  # If the remaining number is 1, it's ugly; otherwise, it's not
  n == 1

end