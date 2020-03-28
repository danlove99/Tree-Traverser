from treeLogo import treelogo
class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Tree:
	def __init__(self, root):
		self.root = Node(root)

	def append(self, val, root):
		if val > root.val:
			if root.right != None:
				self.append(val, root.right)
			else:
				root.right = Node(val)

		elif val < root.val:
			if root.left != None:
				self.append(val, root.left)
			else:
				root.left = Node(val)

	def preorder(self, start, traversal):
		if start:
			traversal += str(start.val) + ' - '
			traversal = self.preorder(start.left, traversal)
			traversal = self.preorder(start.right, traversal)
		return traversal

	def inorder(self, start, traversal):
		if start:
			traversal = self.preorder(start.left, traversal)
			traversal += str(start.val) + ' - '
			traversal = self.preorder(start.right, traversal)
		return traversal

	def postorder(self, start, traversal):
		if start:
			traversal = self.preorder(start.left, traversal)
			traversal = self.preorder(start.right, traversal)
			traversal += str(start.val) + ' - '
		return traversal


	def __str__(self):
		x = input('How would you like to traverse the tree?: \n')
		if x == 'preorder':
			return self.preorder(self.root, '')
		elif x == 'inorder':
			return self.inorder(self.root, '')
		elif x =='postorder':
			return self.postorder(self.root, '')



'''
tree = Tree(5)
tree.append(6, tree.root)
tree.append(4, tree.root)
print(treelogo)
print(tree)'''
