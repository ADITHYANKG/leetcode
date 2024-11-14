// binary string x is valid if all 
// substring  of x of length 2 contain at least one "1".
// Return all valid strings with length n, in any order.
// Example 1:
// Input:  = 3
// Output: ["010","011","101","110","111"]
// Explanation:
// The valid strings of length 3 are: "010", "011", "101", "110", and "111".
var validStrings = function(n) {
     k=(2**n)-1
     res=[]
     if(n>1){
        for(i=1;i<=k;i++){
            b=''
       
            d=i
            while(d>0){
                b=(d%2)+b
                out=b
               if(b.length<n){
                   out=b.padStart(n,"0")
               }
               d=Math.floor(d/2)
            }
            
            a=true
            for(m=0;m<out.length-1;m++){
               if(out.slice(m,m+2)=="00"){
                  a=false
                  
                }
            }
            if(a){
               res.push(out)
            }
            
   
            
        } 
   
       return res
     }
     else{
        retrun ['0','1']
     }
     
};
console.log(validStrings(3))