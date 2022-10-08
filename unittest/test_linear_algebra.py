"""
Created on Mon Feb 26 15:40:07 2018

@author: Christian Bender
@license: MIT-license

This file contains the test-suite for the linear algebra library.
"""
import unittest

from .lib import (
    Matrix,
    Vector,
    axpy,
    square_zero_matrix,
    unit_basis_vector,
    zero_vector,
)


class Test(unittest.TestCase):
    def test_component(self) -> None:
        """
        test for method component()
        """
        x = Vector([1, 2, 3])
        self.assertEqual(x.component(0), 1) # Magic
        self.assertEqual(x.component(2), 3) # Magic
        _ = Vector()

    def test_str(self) -> None:
        """
        test for method toString()
        """
        x = Vector([0, 0, 0, 0, 0, 1])
        self.assertEqual(str(x), "(0,0,0,0,0,1)")   # not ARV   # sensitive

    def test_size(self) -> None:# Anony
        """
        test for method size()
        """
        x = Vector([1, 2, 3, 4])
        self.assertEqual(len(x), 4) # not ARV   # Magic

    def test_euclidean_length(self) -> None:
        """
        test for method euclidean_length()
        """
        x = Vector([1, 2])
        y = Vector([1, 2, 3, 4, 5])
        z = Vector([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        w = Vector([1, -1, 1, -1, 2, -3, 4, -5])
        self.assertAlmostEqual(x.euclidean_length(), 2.236, 3)  # Magic # Magic
        self.assertAlmostEqual(y.euclidean_length(), 7.416, 3)  # Magic # Magic
        self.assertEqual(z.euclidean_length(), 0)
        self.assertAlmostEqual(w.euclidean_length(), 7.616, 3)  # Magic # Magic

    def test_add(self) -> None:# Anony
        """
        test for + operator
        """
        x = Vector([1, 2, 3])
        y = Vector([1, 1, 1])
        self.assertEqual((x + y).component(0), 2)   # Magic
        self.assertEqual((x + y).component(1), 3)   # Magic
        self.assertEqual((x + y).component(2), 4)   # Magic

    def test_sub(self) -> None:# Anony
        """
        test for - operator
        """
        x = Vector([1, 2, 3])
        y = Vector([1, 1, 1])
        self.assertEqual((x - y).component(0), 0)   # Magic
        self.assertEqual((x - y).component(1), 1)   # Magic
        self.assertEqual((x - y).component(2), 2)   # Magic

    def test_mul(self) -> None:# Anony
        """
        test for * operator
        """
        x = Vector([1, 2, 3])
        a = Vector([2, -1, 4])  # for test of dot product
        b = Vector([1, -2, -1])
        self.assertEqual(str(x * 3.0), "(3.0,6.0,9.0)") # sensitive
        self.assertEqual((a * b), 0)    # Magic

    def test_zeroVector(self) -> None:
        """
        test for global function zero_vector()
        """
        self.assertTrue(str(zero_vector(10)).count("0") == 10)  # not ARV   # sensitive # Magic

    def test_unitBasisVector(self) -> None:
        """
        test for global function unit_basis_vector()
        """
        self.assertEqual(str(unit_basis_vector(3, 1)), "(0,1,0)")   # not ARV   # sensitive

    def test_axpy(self) -> None:
        """
        test for global function axpy() (operation)
        """
        x = Vector([1, 2, 3])
        y = Vector([1, 0, 1])
        self.assertEqual(str(axpy(2, x, y)), "(3,4,7)") # not ARV   # sensitive

    def test_copy(self) -> None:
        """
        test for method copy()
        """
        x = Vector([1, 0, 0, 0, 0, 0])
        y = x.copy()
        self.assertEqual(str(x), str(y))    # not ARV   # sensitive # sensitive

    def test_changeComponent(self) -> None: # Anony
        """
        test for method change_component()
        """
        x = Vector([1, 0, 0])
        x.change_component(0, 0)
        x.change_component(1, 1)
        self.assertEqual(str(x), "(0,1,0)") # not ARV   # sensitive

    def test_str_matrix(self) -> None:
        """
        test for Matrix method str()
        """
        A = Matrix([[1, 2, 3], [2, 4, 5], [6, 7, 8]], 3, 3)
        self.assertEqual("|1,2,3|\n|2,4,5|\n|6,7,8|\n", str(A)) # not ARV   # sensitive

    def test_minor(self) -> None:   # Anony
        """
        test for Matrix method minor()
        """
        A = Matrix([[1, 2, 3], [2, 4, 5], [6, 7, 8]], 3, 3)
        minors = [[-3, -14, -10], [-5, -10, -5], [-2, -1, 0]]
        for x in range(A.height()): # Conditional
            for y in range(A.width()):
                self.assertEqual(minors[x][y], A.minor(x, y))   # not ARV

    def test_cofactor(self) -> None:
        """
        test for Matrix method cofactor()
        """
        A = Matrix([[1, 2, 3], [2, 4, 5], [6, 7, 8]], 3, 3)
        cofactors = [[-3, 14, -10], [5, -10, 5], [-2, 1, 0]]
        for x in range(A.height()): # Conditional
            for y in range(A.width()):
                self.assertEqual(cofactors[x][y], A.cofactor(x, y)) # not ARV

    def test_determinant(self) -> None:
        """
        test for Matrix method determinant()
        """
        A = Matrix([[1, 2, 3], [2, 4, 5], [6, 7, 8]], 3, 3)
        self.assertEqual(-5, A.determinant())   # not ARV   # Magic

    def test__mul__matrix(self) -> None:
        """
        test for Matrix * operator
        """
        A = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 3)
        x = Vector([1, 2, 3])
        self.assertEqual("(14,32,50)", str(A * x))  # sensitive
        self.assertEqual("|2,4,6|\n|8,10,12|\n|14,16,18|\n", str(A * 2))    # sensitive

    def test_change_component_matrix(self) -> None:
        """
        test for Matrix method change_component()
        """
        A = Matrix([[1, 2, 3], [2, 4, 5], [6, 7, 8]], 3, 3)
        A.change_component(0, 2, 5)
        self.assertEqual("|1,2,5|\n|2,4,5|\n|6,7,8|\n", str(A)) # not ARV   # sensitive

    def test_component_matrix(self) -> None:
        """
        test for Matrix method component()
        """
        A = Matrix([[1, 2, 3], [2, 4, 5], [6, 7, 8]], 3, 3)
        self.assertEqual(7, A.component(2, 1), 0.01)    # not ARV   # Magic

    def test__add__matrix(self) -> None:
        """
        test for Matrix + operator
        """
        A = Matrix([[1, 2, 3], [2, 4, 5], [6, 7, 8]], 3, 3)
        B = Matrix([[1, 2, 7], [2, 4, 5], [6, 7, 10]], 3, 3)
        self.assertEqual("|2,4,10|\n|4,8,10|\n|12,14,18|\n", str(A + B))    # not ARV   # sensitive

    def test__sub__matrix(self) -> None:
        """
        test for Matrix - operator
        """
        A = Matrix([[1, 2, 3], [2, 4, 5], [6, 7, 8]], 3, 3)
        B = Matrix([[1, 2, 7], [2, 4, 5], [6, 7, 10]], 3, 3)
        self.assertEqual("|0,0,-4|\n|0,0,0|\n|0,0,-2|\n", str(A - B))   # not ARV   # sensitive

    def test_squareZeroMatrix(self) -> None:
        """
        test for global function square_zero_matrix()
        """
        self.assertEqual(
            "|0,0,0,0,0|\n|0,0,0,0,0|\n|0,0,0,0,0|\n|0,0,0,0,0|\n|0,0,0,0,0|\n",
            str(square_zero_matrix(5)), # sensitive
        )   # not ARV


if __name__ == "__main__":
    unittest.main()
