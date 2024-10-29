/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    
    if(x>0){
    let rev=0
    while(x>0){

            d=x%10;
            rev=(rev)*10+d
            x=Math.floor(x/10)
            

    }
    return rev<2**31? rev:0

    }else{
    x=Math.abs(x)    
    let rev=0
    while(x>0){

            d=x%10;
            rev=(rev)*10+d
            x=Math.floor(x/10)       
    }
    return    (-1*rev)> -1*(2**31)?(-1*rev):0
    
    
}



    
    };