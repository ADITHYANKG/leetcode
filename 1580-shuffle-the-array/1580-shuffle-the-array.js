/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number[]}
 */
var shuffle = function(nums, n) {
    res=[]
    for(i=0;i<n;i++){
         res.push(nums[i],nums[i+n])   


    }
    return res
};