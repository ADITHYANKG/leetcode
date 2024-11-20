/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var stringHash = function(s, k) {
    res=""
    for(j=0;j<s.length;j=j+k){
          hash=0
          console.log(j)
          for(i=j;i<j+k;i++){

          hash+=s.charCodeAt(i)-97
         

    }
    rem=hash%26
    res+=String.fromCharCode(rem+97)
}
   
    return res
};
console.log(stringHash("abcd",2))