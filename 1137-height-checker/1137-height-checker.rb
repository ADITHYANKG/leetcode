# @param {Integer[]} heights
# @return {Integer}
def height_checker(heights)
    expected=heights.sort
    res=[]
    for i in 0...heights.length
        if heights[i]!=expected[i]
           res <<i
         end
    end
    return res.length      
end