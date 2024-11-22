/**
 * @param {string} s
 * @return {string[]}
 */
var printVertically = function(s) {
     t=s.split(" ")
     res=[]
     len=[]
     for(i=0;i<t.length;i++){
        
        len.push(t[i].length)
     }
     max=Math.max(...len) 
     console.log(max)
     nt=[]
     for(i=0;i<t.length;i++){
        
          nt.push( t[i].padEnd(max," "))
     }
     
     for(i=0;i<nt[0].length;i++){
        temp=""
        for(j=0;j<nt.length;j++){
        console.log(nt[j][i])
          temp+=nt[j][i]
        
        }
        temp=temp.trimEnd()
        res.push(temp)
     }
     
     return res
};