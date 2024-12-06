/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    for(i=0;i<haystack.length;i++){
        for(j=i+1;j<haystack.length+1;j++){
           if(haystack.slice(i,j)==needle){
            return i
           }
        }

    }
    return -1
};