#
# @Author : Anupam Sharma (anu.lnmiit.1985@gmail.com)
# Problem : You have been given a tree with one extra pointer sibling. For one 
# particular You need to make it point to the right sibling of the nodes for
# that particular node.
#
class TreeNode(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.sibling = None		
	def __str__(self):
		return str(self.value)

root = TreeNode(24)
print TreeNode
#                             24
#                  15                     26
#                     10               25           
#
#
#
root.left = TreeNode(15)
root.right = TreeNode(26)

root.left.right = TreeNode(10)
root.right.left = TreeNode(25)

current_height = {}


def postorder(node, height):
	if node is None:
		return
	height = height + 1
	if height not in current_height:
		current_height[height] = node
	else:
		current_height[height].sibling = node
 		current_height[height] = node

	postorder(node.left, height)
	postorder(node.right, height)

postorder(root.left, 0)
postorder(root.right, 0)

def inorder(node):
	if node is None:
		return
	inorder(node.left)
	print node, node.sibling
	inorder(node.right)

print """
                             24
                  15                     26
                     10               25           

"""
inorder(root)

