import unittest
from stacks import Stacks
 
class TestStacks(unittest.TestCase):

    def setUp(self):   
        self.stacks = Stacks() 
    
    def tearDown(self): 
        self.stacks = None
 
    def test_stack1(self):
        self.stacks.l_push1(1)
        self.stacks.l_push1(2)
        self.stacks.r_push1(3)
        self.stacks.r_push1(4)
        self.assertEqual(self.stacks.l_pop1(), 2)
        self.assertEqual(self.stacks.l_pop1(), 1)
        self.assertEqual(self.stacks.r_pop1(), 4)
        self.assertEqual(self.stacks.r_pop1(), 3)
        self.assertEqual(self.stacks.l_pop1(), 'Stack1 is empty.')
        self.assertEqual(self.stacks.r_pop1(), 'Stack1 is empty.')
    
    def test_stack2(self):
        self.stacks.l_push2(1)
        self.stacks.l_push2(2)
        self.stacks.r_push2(3)
        self.stacks.r_push2(4)
        self.assertEqual(self.stacks.l_pop2(), 2)
        self.assertEqual(self.stacks.l_pop2(), 1)
        self.assertEqual(self.stacks.r_pop2(), 4)
        self.assertEqual(self.stacks.r_pop2(), 3)
        self.assertEqual(self.stacks.l_pop2(), 'Stack2 is empty.')
        self.assertEqual(self.stacks.r_pop2(), 'Stack2 is empty.')
    
    def test_two_stacks(self):
        self.stacks.l_push1(1)
        self.stacks.l_push2(2)
        self.stacks.r_push1(3)
        self.stacks.r_push2(4)
        self.assertEqual(self.stacks.l_pop1(), 1)
        self.assertEqual(self.stacks.r_pop1(), 3)
        self.assertEqual(self.stacks.l_pop1(), 'Stack1 is empty.')
        self.assertEqual(self.stacks.r_pop1(), 'Stack1 is empty.')
        self.assertEqual(self.stacks.l_pop2(), 2)
        self.assertEqual(self.stacks.r_pop2(), 4)
        self.assertEqual(self.stacks.l_pop2(), 'Stack2 is empty.')
        self.assertEqual(self.stacks.r_pop2(), 'Stack2 is empty.')
 
def suite(): 
  suite = unittest.TestSuite() 
  suite.addTest(TestStacks('test_stack1'))
  suite.addTest(TestStacks('test_stack2'))
  suite.addTest(TestStacks('test_two_stacks'))
  return suite

if __name__ == "__main__":
    unittest.main(defaultTest = 'suite')
