#!/usr/bin/env python
# coding: utf-8

# In[1]:


import unittest
import checkmates
from checkmates import testfigure
from checkmates import CheckException

class CheckmatesTest(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual("Normal", testfigure(1,1,5,5,8,8),'Should be Normal')
    def test_case_2(self):
        self.assertEqual("Check", testfigure(1,1,5,5,1,5),'Should be Check')
    def test_case_3(self):
        self.assertEqual("Checkmate", testfigure(1,1,3,4,1,4),'Should be Checkmate')
    def test_case_4(self):
        self.assertEqual("Stalemate", testfigure(2,2,3,3,1,1),'Should be Stalemate')
    def test_case_5(self):
        self.assertEqual("Strange", testfigure(1,1,5,5,5,6),'Should be Strange')
    def test_case_6(self):
        self.assertEqual("Strange", testfigure(4,4,5,4,6,4),'Should be Strange')
    def test_case_7(self):
        self.assertEqual("Stalemate", testfigure(7,7,6,6,8,8),'Should be Stalemate')
    def test_case_8(self):
        self.assertEqual("Stalemate", testfigure(7,7,6,7,8,8),'Should be Stalemate')
    def test_case_9(self):
        self.assertEqual("Stalemate", testfigure(7,7,6,8,8,8),'Should be Stalemate')
    def test_case_10(self):
        self.assertEqual("Strange", testfigure(7,7,7,8,8,8),'Should be Strange')
    def test_case_11(self):
        self.assertEqual("Checkmate", testfigure(1,8,3,1,1,1),'Should be Checkmate')
    def test_case_12(self):
        self.assertEqual("Normal", testfigure(1,8,1,3,1,1),'Should be Normal')
    def test_case_13(self):
        self.assertEqual("Normal", testfigure(1,8,1,4,1,1),'Should be Normal')
    def test_case_14(self):
        self.assertEqual("Checkmate", testfigure(8,1,1,3,1,1),'Should be Checkmate')
    def test_case_15(self):
        self.assertEqual("Normal", testfigure(1,8,1,3,1,1),'Should be Normal')
    def test_case_16(self):
        self.assertEqual("Check", testfigure(2,8,1,6,1,8),'Should be Check')
    def test_case_17(self):
        self.assertEqual("Checkmate", testfigure(3,8,1,6,1,8),'Should be Checkmate')
    def test_case_18(self):
        self.assertEqual("Check", testfigure(1,7,1,6,1,8),'Should be Check')
    def test_case_19(self):
        self.assertEqual("Checkmate", testfigure(8,1,6,8,8,8),'Should be Checkmate')
    def test_case_20(self):
        self.assertEqual("Checkmate", testfigure(1,8,8,6,8,8),'Should be Checkmate')
    def test_case_21(self):
        self.assertEqual("Normal", testfigure(1,7,8,6,8,8),'Should be Normal')
    def test_case_22(self):
        self.assertEqual("Checkmate", testfigure(1,1,8,3,8,1),'Should be Checkmate')
    def test_case_23(self):
        self.assertEqual("Checkmate", testfigure(8,8,6,1,8,1),'Should be Checkmate')
    def test_case_24(self):
        self.assertEqual("Check", testfigure(8,2,6,1,8,1),'Should be Check')
    def test_case_25(self):
        self.assertEqual("Check", testfigure(7,1,6,1,8,1),'Should be Check')
    def test_case_26(self):
        self.assertEqual("Normal", testfigure(5,1,6,1,8,1),'Should be Normal')

if __name__ == '__main__':
    unittest.main()
        


# In[ ]:
