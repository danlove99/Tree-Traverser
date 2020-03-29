from treeLogo import treelogo
from Help import help

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
		print('''
			Available traversals:
			preorder
			inorder
			postorder'''
			)
		x = input('How would you like to traverse the tree?: \n')
		if x == 'preorder':
			return self.preorder(self.root, '')
		elif x == 'inorder':
			return self.inorder(self.root, '')
		elif x =='postorder':
			return self.postorder(self.root, '')

trees = []


def newTree():
	if len(trees) > 0:
		print('You already have a tree...\n type deleteTree to create another one')
		return
	root = input('what would you like the root of the tree to be?: ')
	tree1 = Tree(root)
	trees.append(tree1)


def append():
	if len(trees) <= 0:
		print('No tree to append to!\n')
		return
	curTree = trees[0]
	val = input('what value do you want to append to the tree?')
	curTree.append(val, curTree.root)
	return

if __name__ == "__main__":
    print(treelogo)
    print('type help for a list of commands\n')
    command = ''
    while(command != 'exit'):
        command = input()
        if command == 'help':
            print(help)
        elif command == 'newTree':
        	newTree()
        elif command == 'append':
        	append()
        elif command == 'traverse':
        	if len(trees) <= 0:
        		print('No tree to append to!\n')
        	print(trees[0])
        elif command == 'deleteTree':
        	trees.pop()


        
    exit()
    



'''
tree = Tree(5)
tree.append(6, tree.root)
tree.append(4, tree.root)
print(treelogo)
print(tree)'''
