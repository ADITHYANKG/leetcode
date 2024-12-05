/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
     s1=s.trim()
     ar=s1.split(" ")
     return ar[ar.length-1].length
    };