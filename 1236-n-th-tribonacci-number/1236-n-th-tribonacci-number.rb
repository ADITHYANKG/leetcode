# @param {Integer} n
# @return {Integer}
def tribonacci(n)
    a=0
    b=1
    c=1
    if n==0
     return a
    elsif n==2 or n==1
    return b
    else
     for i in  1...n-1
      d=a+b+c
      a=b
      b=c
      c=d
      end
     return c
    end
end