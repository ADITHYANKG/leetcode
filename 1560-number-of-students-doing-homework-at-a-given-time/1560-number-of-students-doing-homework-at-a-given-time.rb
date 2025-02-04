# @param {Integer[]} start_time
# @param {Integer[]} end_time
# @param {Integer} query_time
# @return {Integer}
def busy_student(start_time, end_time, query_time)
   c=0
    for i in 0...start_time.length
        if query_time>=start_time[i] and end_time[i]>=query_time
            c+=1
        end
        end
        c    
end