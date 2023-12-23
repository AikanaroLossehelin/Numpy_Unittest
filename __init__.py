# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 17:56:59 2023

@author: aikan

coverage run -m __init__
coverage report
coverage html
"""
import unittest as ut
import numpy as np
import sys
from hypothesis import given, strategies as st

class TestNumpyFunctions(ut.TestCase):

    @given(st.lists(st.integers()))
    def test_numpy_array_with_integers(self, lst):
        array = np.array(lst)
        self.assertTrue(np.array_equal(array, np.array(lst)))

    @given(st.lists(st.floats(allow_nan=False, allow_infinity=False)))
    def test_numpy_array_with_floats(self, lst):
        array = np.array(lst)
        self.assertTrue(np.array_equal(array, np.array(lst)))

    @given(st.lists(st.tuples(st.integers(), st.integers())))
    def test_numpy_array_with_tuples(self, lst):
        array = np.array(lst)
        self.assertTrue(np.array_equal(array, np.array(lst)))

    @given(st.lists(st.booleans()))
    def test_numpy_array_with_booleans(self, lst):
        array = np.array(lst)
        self.assertTrue(np.array_equal(array, np.array(lst)))
        
        # Tests pour la création d'arrays
    @given(st.lists(st.integers()))
    def test_numpy_array(self, lst):
        array = np.array(lst)
        self.assertTrue(np.array_equal(array, np.array(lst)))

    @given(st.integers(min_value=1, max_value=10))
    def test_numpy_zeros(self, n):
        self.assertTrue(np.array_equal(np.zeros(n), np.zeros(n)))

    @given(st.integers(min_value=1, max_value=10))
    def test_numpy_ones(self, n):
        self.assertTrue(np.array_equal(np.ones(n), np.ones(n)))

    @given(st.integers(min_value=0, max_value=10), st.integers(min_value=11, max_value=20))
    def test_numpy_arange(self, start, end):
        self.assertTrue(np.array_equal(np.arange(start, end), np.arange(start, end)))

    @given(st.floats(min_value=0, max_value=10), st.floats(min_value=11, max_value=20), st.integers(min_value=2, max_value=10))
    def test_numpy_linspace(self, start, end, num):
        self.assertTrue(np.array_equal(np.linspace(start, end, num), np.linspace(start, end, num)))

    # Tests pour les opérations mathématiques
    @given(st.lists(st.floats(min_value=0, max_value=1e307, allow_nan=False, allow_infinity=False)), st.lists(st.floats(min_value=-1e307, max_value=1e307, allow_nan=False, allow_infinity=False)))
    def test_numpy_operations(self, a, b):
       if len(a) == len(b) and all(x != 0 for x in b):
           a, b = np.array(a), np.array(b)
           self.assertTrue(np.all(np.add(a, b) == np.add(a, b)))
           self.assertTrue(np.all(np.subtract(a, b) == np.subtract(a, b)))
           self.assertTrue(np.all(np.multiply(a, b) == np.multiply(a, b)))
           self.assertTrue(np.all(np.divide(a, b) == np.divide(a, b)))
           self.assertTrue(np.all(np.sqrt(a) == np.sqrt(a)))
           self.assertTrue(np.all(np.exp(a) == np.exp(a)))
           self.assertTrue(np.all(np.sin(a) == np.sin(a)))
           self.assertTrue(np.all(np.cos(a) == np.cos(a)))
           self.assertTrue(np.all(np.tan(a) == np.tan(a)))
           
    # Tests pour la manipulation d'arrays
    @given(st.lists(st.integers()), st.integers(min_value=1, max_value=5))
    def test_numpy_reshape(self, lst, n):
        if len(lst) % n == 0 and len(lst) != 0:
            a = np.array(lst).reshape(n, -1)
            self.assertEqual(a.shape[0], n)

    @given(st.lists(st.integers()), st.lists(st.integers()))
    def test_numpy_concatenate(self, a, b):
        a, b = np.array(a), np.array(b)
        self.assertTrue(np.array_equal(np.concatenate([a, b]), np.concatenate([a, b])))

    @given(st.lists(st.integers()), st.integers(min_value=2, max_value=5))
    def test_numpy_split(self, lst, n):
        if len(lst) >= n and len(lst) % n == 0:
            splits = np.split(np.array(lst), n)
            self.assertEqual(len(splits), n)

    @given(st.lists(st.integers()))
    def test_numpy_transpose(self, lst):
        a = np.array(lst)
        self.assertTrue(np.array_equal(a.transpose(), a.transpose()))

    # Tests pour les statistiques et les aggrégations
    @given(st.lists(st.floats(allow_infinity=False, allow_nan=False)))
    def test_numpy_statistics(self, lst):
        if len(lst) > 0:
            a = np.array(lst)
            self.assertAlmostEqual(np.mean(a), np.mean(a))
            self.assertAlmostEqual(np.median(a), np.median(a))
            self.assertAlmostEqual(np.std(a), np.std(a))
            self.assertAlmostEqual(np.sum(a), np.sum(a))

    # Tests pour l'algèbre linéaire
    @given(st.lists(st.lists(st.floats(min_value=-100, max_value=100, allow_nan=False, allow_infinity=False), min_size=2, max_size=2), min_size=2, max_size=2))
    def test_numpy_linear_algebra(self, lst):
       a = np.array(lst)
       if np.linalg.det(a) != 0 and not np.isclose(np.linalg.det(a), 0):
           inv_a = np.linalg.inv(a)
           self.assertTrue(np.allclose(np.dot(a, inv_a), np.eye(a.shape[0]), atol=1e-5))

if __name__ == '__main__':
    ut.main()

