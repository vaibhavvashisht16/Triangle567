# -*- coding: utf-8 -*-
"""
Updated Sept 18,2021 - TestTriangle;
The primary goal of this file is to demonstrate a simple unittest implementation

@author: Vaibhav Vashisht
"""
# This code implements the unit test functionality

import unittest
from Triangle import classifyTriangle

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testInvalidInput(self):
        self.assertEqual(classifyTriangle(-2, 1, 4), 'InvalidInput', '-2,1,4 is a Not a Invalid input')

    def testInvalidInput2(self):
        self.assertEqual(classifyTriangle(0,0,0), 'InvalidInput', '0,0,0 is Not a Invalid input')

    def testInvalidInput3(self):
        self.assertNotEqual(classifyTriangle(200,400,300), 'InvalidInput', '200,400,300 is Not a Invalid input')

    def testNotaTriangle1(self):
        self.assertEqual(classifyTriangle(1, 10, 12), "NotATriangle", "Should be Not a Triangle")

    def testNotaTriangle2(self):
        self.assertNotEqual(classifyTriangle(3, 1.5, 1.5), "Equilateral", "Should be Not a Triangle")

    def testNotaTriangle3(self):
        self.assertNotEqual(classifyTriangle(1, 1, 2), "Isosceles", "Should be Not a Triangle")

    def testNotaTriangle4(self):
        self.assertNotEqual(classifyTriangle(1, 4, 6), "Scalene", "Should be Not a Triangle")

    def testNotaTriangle5(self):
        self.assertNotEqual(classifyTriangle(4, 2, 6), "Right", "Should be Not a Triangle")

    def testRightTriangleA1(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3, 4, 5 should be Right Triangle')

    def testRightTriangleA2(self):
        self.assertNotEqual(classifyTriangle(12, 13, 5), "Isosceles", "Should be Right")

    def testRightTriangleA3(self):
        self.assertNotEqual(classifyTriangle(10, 6, 8), "Equilateral", "Should be Right")

    def testRightTriangleA4(self):
        self.assertNotEqual(classifyTriangle(4, 3, 5), "NotATriangle", "Should be Right")

    def testRightTriangle5(self):
        self.assertNotEqual(classifyTriangle(12, 13, 5), "Scalene", "Should be Right")

    def testIsoscelesTriangle1(self):
        self.assertEqual(classifyTriangle(3, 3, 5), 'Isosceles', '5,3,4 is a Isosceles triangle')

    def testIsoscelesTriangle2(self):
        self.assertNotEqual(classifyTriangle(4, 2, 2), "Scalene", "Should be Isosceles")

    def testIsoscelesTriangle4(self):
        self.assertNotEqual(classifyTriangle(5, 9, 5), 'Right', 'Should be Isosceles')

    def testIsoscelesTriangle3(self):
        self.assertNotEqual(classifyTriangle(5, 5, 3), "Equilateral", "Should be Isosceles")

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(3, 10, 12), "Scalene", "Should be Scalene")

    def testScaleneTriangle1(self):
        self.assertNotEqual(classifyTriangle(1, 3, 2), "Isosceles", "Should be Scalene")

    def testScaleneTriangle2(self):
        self.assertNotEqual(classifyTriangle(3, 4, 1.5), "Equilateral", "Should be Scalene")

    def testScaleneTriangle3(self):
        self.assertNotEqual(classifyTriangle(4, 2, 6), "Right", "Should be Scalene")

    def testScaleneTriangle4(self):
        self.assertNotEqual(classifyTriangle(3, 4, 7), "Not a Triangle", "Should be Scalene")

    def testEquilateralTriangle1(self):
        self.assertEqual(classifyTriangle(1, 1, 1), "Equilateral", "Should be Equilateral")

    def testEquilateralTriangle2(self):
        self.assertNotEqual(classifyTriangle(6, 6, 6), "Right", "Should be Equilateral")

    def testEquilateralTriangle2(self):
        self.assertNotEqual(classifyTriangle(1.5, 1.5, 1.5), "Not a Triangle", "Should be Equilateral")




