import unittest
from largesum import LargeSum
 
class TestLargeSum(unittest.TestCase):

    def setUp(self):   
        self.the_sum = LargeSum() 
    
    def tearDown(self): 
        self.the_sum = None
 
    def test_sum1(self):
        x = '999999999999999999999999999999999999999'
        y = '888888888888888888888888888888888888888'
        z = '1888888888888888888888888888888888888887'
        self.assertEqual(self.the_sum.large_sum(x, y), z)
    
    def test_sum2(self):
        x = '999999999999999999999999999999999999999'
        y = '99999999999999999999999999999999999999'
        z = '1099999999999999999999999999999999999998'
        self.assertEqual(self.the_sum.large_sum(x, y), z)
    
    def test_sum3(self):
        x = '5555555555555555555555555555555555555'
        y = '555555555555555555555555555555555555555'
        z = '561111111111111111111111111111111111110'
        self.assertEqual(self.the_sum.large_sum(x, y), z)
    
def suite(): 
  suite = unittest.TestSuite() 
  suite.addTest(TestLargeSum('test_sum1'))
  suite.addTest(TestLargeSum('test_sum2'))
  suite.addTest(TestLargeSum('test_sum3'))
  return suite

if __name__ == "__main__":
    unittest.main(defaultTest = 'suite')
