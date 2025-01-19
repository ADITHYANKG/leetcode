# @param {String[][]} paths
# @return {String}
def dest_city(paths)
res=true
    for i in 0...paths.length
    res=true
        for j in 0...paths.length
            if j==i
             next
            end
            if paths[i][1]==paths[j][0] 
                res=false
            end
         end

        if res==true 
         out=paths[i][1] 
        end

    end 
    out          
end