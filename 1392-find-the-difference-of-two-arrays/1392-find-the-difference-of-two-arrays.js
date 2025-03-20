/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[][]}
 */
var findDifference = function(nums1, nums2) {
    res=[]
    temp1=[]
    for(i=0;i<nums1.length;i++){
        
        c=true
        for(j=0;j<nums2.length;j++){
            if(nums1[i]==nums2[j]){
                c=false
                break
            }
        }
        if(c==true){
            temp1.push(nums1[i])
        }
    }
    temp2=[]
    for(i=0;i<nums2.length;i++){
        
        d=true
        for(j=0;j<nums1.length;j++){
            if(nums2[i]==nums1[j]){
                d=false
                break
            }
        }
        if(d==true){
            temp2.push(nums2[i])
        }
    }
    t1=[...new Set(temp1)]
    t2=[...new Set(temp2)]
    return[t1,t2]
};