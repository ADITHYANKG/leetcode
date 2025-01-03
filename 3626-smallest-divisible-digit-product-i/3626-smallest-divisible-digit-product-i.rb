# @param {Integer} n
# @param {Integer} t
# @return {Integer}
def smallest_number(n, t)
    def digit_product(x)
    x.to_s.chars.map(&:to_i).reduce(1, :*)
  end
      current = n
  while true
    if digit_product(current) % t == 0
      return current
    end
    current += 1
  end
end