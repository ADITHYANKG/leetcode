# @param {Integer[][]} mat
# @return {Integer}
def diagonal_sum(mat)
      sum=0
     for i in 0...mat.length
          if i!=mat.length-1-i
         sum+=mat[i][i]+mat[i][mat.length-1-i] 
         else
         sum+=mat[i][i]
         end

    end
    sum
end