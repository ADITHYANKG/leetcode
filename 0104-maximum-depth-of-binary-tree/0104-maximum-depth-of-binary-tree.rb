# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {TreeNode} root
# @return {Integer}
def max_depth(root)
     # Base case: if the tree is empty
  return 0 if root.nil?

  # Recursively compute the depth of the left and right subtrees
  left_depth = max_depth(root.left)
  right_depth = max_depth(root.right)

  # The depth of the current node is 1 + the maximum of the left and right depths
  [left_depth, right_depth].max + 1
end