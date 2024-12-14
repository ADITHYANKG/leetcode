# @param {String} s
# @return {Boolean}
def is_palindrome(s)
    a=s.split(" ")
	s=a.join("")

	res=""
    for i in 0...s.length
    	if ( s[i].ord<=90 and s[i].ord>=65 )or (s[i].ord<=122 and s[i].ord>=97) or (s[i].ord<=57 and s[i].ord>=48)
               res+=s[i].downcase
               res+=s[i].downcase
         end
 	end
     res.reverse==res ?  true : false
end
