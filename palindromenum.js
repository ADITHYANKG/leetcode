/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    n=x
    rev=0
    while(n>0){
        
        d=n%10
        rev=rev*10+d
        n=Math.floor(n/10)


    }
    return rev==x?true:false
  

    
};