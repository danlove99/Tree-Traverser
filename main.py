from treeLogo import treelogo
from Help import help
from Tree import *

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
	val = input('what value do you want to append to the tree?: ')
	curTree.append(val, curTree.root)
	return

def traversal():
	if len(trees) <= 0:
		print('No tree to traverse!\n')
		return
	print(trees[0])

def height():
	if len(trees) <= 0:
		print('no tree to measure!\n')
		return
	curTree = trees[0]
	print(curTree.height(curTree.root))
def size():
	print(trees[0].size())
	print(trees[0].size_(trees[0].root))

def reverse():
	if len(trees) <= 0:
		print('no tree to reverse')
		return
	print(trees[0].reverse(trees[0].root))

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
            traversal()
        elif command == 'deleteTree':
            trees.pop()
        elif command == 'height':
            height()
        elif command == 'size':
            size()
        elif command == 'exit':
            print('goodbye!')
        elif command == 'reverse':
        	reverse()
        else:
        	print('command not recognised!')



        
    exit()
    
