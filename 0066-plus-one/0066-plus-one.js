/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    res=""
    for(i=0;i<digits.length;i++){
            res+=digits[i]

    }
    
    temp=BigInt(res)+BigInt(1)
    return String(temp).split("").map(i=>parseInt(i)) 
    
};