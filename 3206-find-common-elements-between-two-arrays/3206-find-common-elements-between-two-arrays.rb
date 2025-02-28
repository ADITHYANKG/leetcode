# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer[]}
def find_intersection_values(nums1, nums2)
    a=0
    b=0
    for i in 0...nums1.length
        for j in 0...nums2.length
            if nums1[i]==nums2[j]
              a+=1
             break 
             end
        end
    end 

     for i in 0...nums2.length
        for j in 0...nums1.length
            if nums2[i]==nums1[j]
              b+=1
             break 
             end
        end
    end 
    [a,b]
end