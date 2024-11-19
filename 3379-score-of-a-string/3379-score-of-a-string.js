/**
 * @param {string} s
 * @return {number}
 */
var scoreOfString = function(s) {
    sum=0
    for(i=0;i<s.length-1;i++){
        sum+=Math.abs(s[i].charCodeAt()-s[i+1].charCodeAt())

    }
    return sum
};