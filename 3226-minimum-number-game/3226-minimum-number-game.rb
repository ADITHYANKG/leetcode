# @param {Integer[]} nums
# @return {Integer[]}
def number_game(nums)
      arr=[]
      nums.sort!
    while nums.length>0
       alice=nums.shift
       bob=nums.shift
        arr <<bob
        arr<<alice
    end    
       arr
end