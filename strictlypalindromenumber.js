var isStrictlyPalindromic = function(n) {
     a=true
     rev=0
     res=[]
     for(i=2;i<=n-2;i++){
      b=''
        dec=n
        
       while(dec>0){
         d=dec%i
         b=d+b

         dec=Math.floor(dec/i)
         
         
       }
       console.log(b)
       console.log(b.split("").reverse().join(''))
       if(b!=b.split("").reverse().join('')){
           a=false
           
       }
       
       
     }
        
    
    // while(n>0){
    //     dig=n%10
    //     rev=rev*10+dig
    //     n=Math.floor(n/10)
    // }
return a
   
}
console.log(isStrictlyPalindromic(10));
