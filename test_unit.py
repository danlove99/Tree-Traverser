import unittest
import main

class TestMethods(unittest.TestCase):
	def setup(self):
		pass


	def test_basics(self):
		main.newTree()
		self.assertGreater(len(main.trees), 0)
		
	
if __name__ == '__main__':
	unittest.main()