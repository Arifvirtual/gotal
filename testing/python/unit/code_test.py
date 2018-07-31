import unittest
from code import *

class MyFirstTests(unittest.TestCase):
  
  def test_hello(self):
    print "--{0}--".format(hello())
    self.assertEqual('Hello, World!', hello())

  def test_bad_hello(self):
    self.assertEqual('Hello, World!', hello())


if __name__ == '__main__':
    import xmlrunner
    #unittest.main()
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))

