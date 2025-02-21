# @param {Integer[][]} mat
# @param {Integer} k
# @return {Integer[][]}
def matrix_block_sum(mat, k)
    m, n = mat.length, mat[0].length
  
  # Step 1: Compute prefix sum matrix
  prefix = Array.new(m+1) { Array.new(n+1, 0) }
  
  (1..m).each do |i|
    (1..n).each do |j|
      prefix[i][j] = mat[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]
    end
  end
  
  # Step 2: Compute block sum using prefix sum matrix
  res = Array.new(m) { Array.new(n, 0) }
  
  (0...m).each do |i|
    (0...n).each do |j|
      r1, c1 = [0, i-k].max, [0, j-k].max
      r2, c2 = [m-1, i+k].min, [n-1, j+k].min

      res[i][j] = prefix[r2+1][c2+1] - prefix[r1][c2+1] - prefix[r2+1][c1] + prefix[r1][c1]
    end
  end

  res
end