var intToRoman = function(num) {
    i=1
    // value={1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
    var rom={0:["I","V","X"],1:["X","L","C"],2:["C","D","M"],3:["M"]}
    j=0
    var res=""
    while(num>0){     
    n=num%(10**i)
    
    if (n >= 1*(10**j) && n <= 3*(10**j)) {
         res=rom[j][0].repeat(Math.floor(n/(10**j)))+res;
    } else if (n === 4*(10**j)) {
         res=rom[j][0]+rom[j][1]+res;
    } else if (n === 5*(10**j)) {
        res=rom[j][1]+res;
    } else if (n >= 6*(10**j) && n <= 8*(10**j)) {
         res=rom[j][1] +rom[j][0] .repeat(Math.floor(n/(10**j))-5)+res;
    } else if(n === 9*(10**j)) {
         res=rom[j][0]+rom[j][2]+res;
    } 
          
    num=num-(num%(10**i))
    i++
    j++  
    }
    return res
};