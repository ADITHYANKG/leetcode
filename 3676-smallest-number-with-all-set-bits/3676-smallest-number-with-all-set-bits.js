/**
 * @param {number} n
 * @return {number}
 */
var smallestNumber = function(n) {
    if(n==1){
        return 1
    }
    for(i=n+1;i<=2*n;i++){
        if(Math.log2(i)==Math.round(Math.log2(i))){
            return i-1
            break
        }
    }
    
};