var sortTheStudents = function(s, k) {
        for(i=0;i<s.length;i++){
               for(j=0;j<s.length-1;j++){
                   if(s[j][k]<s[j+1][k]){
                      temp=s[j+1]
                      s[j+1]=s[j]
                      s[j]=temp
                   }

               }

        }
        return s
};
console.log(sortTheStudents([[3,4],[5,6]],0))