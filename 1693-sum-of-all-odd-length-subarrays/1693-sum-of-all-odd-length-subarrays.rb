# @param {Integer[]} arr
# @return {Integer}
def sum_odd_length_subarrays(arr)
    sum=0
    for i in 0...arr.length
        for j in 0...arr.length
          if arr[i..j].length%2!=0
           sum+=arr[i..j].sum
           end
           end
           end
      sum 
end