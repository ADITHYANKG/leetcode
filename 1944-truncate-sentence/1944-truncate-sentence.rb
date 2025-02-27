# @param {String} s
# @param {Integer} k
# @return {String}
def truncate_sentence(s, k)
    w=s.split
    w[0...k].join(" ")
end