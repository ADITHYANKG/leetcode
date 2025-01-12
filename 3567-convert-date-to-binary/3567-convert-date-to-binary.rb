# @param {String} date
# @return {String}
def convert_date_to_binary(date)
def bin(n)
res=""
  while n>0
   res=(n%2).to_s+res
   n=n/2
  end 
res
end  
    
  final=bin(date[0..3].to_i)+"-"+bin(date[5..6].to_i)+"-"+bin(date[8..9].to_i)  
end