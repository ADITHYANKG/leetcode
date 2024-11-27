/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
//         res=""
//         if(strs.length==1){
//             return strs[0]
//             }
//         for (i=0;i<strs.length+1;i++){
//             c=0
            
//             for(j=1;j<strs.length;j++){
//                 if(strs[0].slice(0,i+2)==strs[j].slice(0,i+2)){
//                     c+=1}

//             }
//             if(c==(strs.length-1)){
//                 res=strs[0].slice(0,i+2)
//                 } 
                
//             }
//   return res       
let res = "";
    if (strs.length === 1) {
        return strs[0];
    }
    for (let i = 0; i < strs[0].length; i++) {
        let c = 0;

        for (let j = 1; j < strs.length; j++) {
            if (strs[0].substring(0, i + 1) === strs[j].substring(0, i + 1)) {
                c++;
            }
        }
        if (c === (strs.length - 1)) {
            res = strs[0].substring(0, i + 1);
        }
    }
    return res;     
} 

   