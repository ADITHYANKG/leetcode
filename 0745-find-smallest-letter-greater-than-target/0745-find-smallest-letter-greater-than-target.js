/**
 * @param {character[]} letters
 * @param {character} target
 * @return {character}
 */
var nextGreatestLetter = function(l, t) {
    
    res=l[0]
    temp=res
    console.log(temp)
      for(i=0;i<l.length;i++){
         if(l[i]<=t){
            l.splice(i,1,"}")
         }

      }
    console.log(l)
    min=t.charCodeAt()
    a="}"
     s=a.charCodeAt()
     
     res=temp
     console.log(res)
     for(i=0;i<l.length;i++){
          if((l[i].charCodeAt()-min)<s-min){
            s=l[i].charCodeAt()-min
            res=l[i]
            
          }

     }
    return res

    
};