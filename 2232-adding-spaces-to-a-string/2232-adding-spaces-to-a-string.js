/**
 * @param {string} s
 * @param {number[]} spaces
 * @return {string}
 */
var addSpaces = function(s, spaces) {
    j=0
    res=""
   for(i=0;i<s.length;i++){
        if(i==spaces[j]){
            res+=" "+s[i]
            j+=1
        }else{
            res+=s[i]
        }
   }
   return res
};