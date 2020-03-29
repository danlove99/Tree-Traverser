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

	def levelorder(self, start):
	    if start is None:
	        return 

	    queue = Queue()
	    queue.enqueue(start)

	    traversal = ""
	    while len(queue) > 0:
	        traversal += str(queue.peek()) + "-"
	        node = queue.dequeue()

	        if node.left:
	            queue.enqueue(node.left)
	        if node.right:
	            queue.enqueue(node.right)

	    return traversal

	def height(self, node):
		if node is None:
			return -1
		left_height = self.height(node.left)
		right_height = self.height(node.right)

		return 1 + max(left_height, right_height)

	def size_(self, node):
		if node is None:
			return 0
		return 1 + self.size_(node.left) + self.size_(node.right)

	def size(self):
		if self.root is None:
			return 0
		stack = Stack()
		stack.push(self.root)
		size = 1
		while stack:
			node = stack.pop()
			if node.left:
				size += 1
				stack.push(node.left)
			if node.right:
				size += 1
				stack.push(node.right)
		return size

	def reverse(self, start):
		if start is None:
			return 
		queue = Queue()
		stack = Stack()
		queue.enqueue(start)
		traversal = ""
		while len(queue) > 0:
			node = queue.dequeue()

			stack.push(node)

			if node.right:
				queue.enqueue(node.right)
			if node.left:
				queue.enqueue(node.left)
        
		while len(stack) > 0:
			node = stack.pop()
			traversal += str(node.val) + "-"

		return traversal


	def __str__(self):
		print('''
			Available traversals:
			preorder
			inorder
			postorder
			levelorder'''
			)
		x = input('How would you like to traverse the tree?: \n')
		if x == 'preorder':
			return self.preorder(self.root, '')
		elif x == 'inorder':
			return self.inorder(self.root, '')
		elif x =='postorder':
			return self.postorder(self.root, '')
		elif x =='levelorder':
			return self.levelorder(self.root)


class Stack:
    def __init__(self):
        self.items = []

    def __len__(self):
        return self.size()
     
    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):  
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        s = ""
        for i in range(len(self.items)):
            s += str(self.items[i].val) + "-"
        return s


class Queue:
    def __init__(self):
        self.items = []

    def __len__(self):
        return self.size()

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].val
