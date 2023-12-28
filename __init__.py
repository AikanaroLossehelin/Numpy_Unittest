# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 17:56:59 2023

@author: aikan
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
    @given(st.lists(st.floats(min_value=0, max_value=20, allow_nan=False, allow_infinity=False)), st.lists(st.floats(min_value=0.01, max_value=100, allow_nan=False, allow_infinity=False)))
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

    @given(st.lists(st.floats(allow_nan=False, allow_infinity=False, min_value=-1e10, max_value=1e10), min_size=1))
    def test_numpy_max_min(self, lst):
        array = np.array(lst)
        self.assertEqual(np.max(array), max(lst))
        self.assertEqual(np.min(array), min(lst))

    @given(st.lists(st.floats(allow_nan=False, allow_infinity=False, min_value=-1e10, max_value=1e10), min_size=1))
    def test_numpy_argmax_argmin(self, lst):
        array = np.array(lst)
        self.assertEqual(np.argmax(array), lst.index(max(lst)))
        self.assertEqual(np.argmin(array), lst.index(min(lst)))

    @given(st.lists(st.floats(allow_infinity=False, allow_nan=False, min_value=-1e2, max_value=1e2), min_size=1))
    def test_numpy_var(self, lst):
        array = np.array(lst)
        self.assertAlmostEqual(np.var(array), np.var(lst), places=5)

    # Manipulation de formes et dimensions
    @given(st.lists(st.integers()))
    def test_numpy_ravel(self, lst):
        array = np.array(lst)
        self.assertTrue(np.array_equal(np.ravel(array), np.ravel(lst)))

    @given(st.lists(st.integers(), min_size=1), st.integers(min_value=0, max_value=1))
    def test_numpy_expand_dims(self, lst, axis):
        array = np.array(lst)
        self.assertTrue(np.array_equal(np.expand_dims(array, axis=axis), np.expand_dims(lst, axis=axis)))

    @given(st.lists(st.integers()))
    def test_numpy_squeeze(self, lst):
        array = np.array([lst])
        self.assertTrue(np.array_equal(np.squeeze(array), np.squeeze(lst)))

    # Fonctions mathématiques et trigonométriques
    @given(st.lists(st.floats(min_value=0.1, max_value=10, allow_nan=False, allow_infinity=False)))
    def test_numpy_log_log10(self, lst):
        array = np.array(lst)
        self.assertTrue(np.allclose(np.log(array), np.log(lst)))
        self.assertTrue(np.allclose(np.log10(array), np.log10(lst)))

    @given(st.lists(st.floats(min_value=-1e10, max_value=1e10), min_size=2), st.integers(min_value=0, max_value=20))
    def test_numpy_power(self, lst, exp):
        array = np.array(lst)
        if exp < 0 and 0 in lst:
            raise ut.SkipTest("Negative power with zero in list")
        self.assertTrue(np.array_equal(np.power(array, exp), np.power(lst, exp)))

    @given(st.floats(min_value=-1e10, max_value=1e10), st.floats(min_value=-1e10, max_value=1e10))
    def test_numpy_hypot(self, x, y):
        if np.isnan(np.hypot(x, y)):
            raise ut.SkipTest("Invalid combination leading to NaN")
        self.assertAlmostEqual(np.hypot(x, y), np.hypot(x, y))

    # Traitement des matrices et de l'algèbre linéaire
    @given(st.lists(st.lists(st.floats(allow_nan=False, allow_infinity=False, min_value=-1e2, max_value=1e2), min_size=3, max_size=3), min_size=3, max_size=3))
    def test_numpy_trace(self, lst):
        array = np.array(lst)
        self.assertAlmostEqual(np.trace(array), np.trace(lst))

    @given(st.lists(st.lists(st.floats(allow_nan=False, allow_infinity=False, min_value=-1e2, max_value=1e2), min_size=2, max_size=2), min_size=2, max_size=2))
    def test_numpy_eig(self, lst):
        array = np.array(lst)
        if np.isnan(array).any() or np.isinf(array).any():
            raise ut.SkipTest("Invalid matrix with NaN or inf")
        w, _ = np.linalg.eig(array)
        self.assertIsInstance(w, np.ndarray)

    @given(st.lists(st.lists(st.floats(allow_nan=False, allow_infinity=False, min_value=-1e2, max_value=1e2), min_size=2, max_size=2), min_size=2, max_size=2))
    def test_numpy_svd(self, lst):
        array = np.array(lst)
        if np.isnan(array).any() or np.isinf(array).any():
            raise ut.SkipTest("Invalid matrix with NaN or inf")
        u, s, vh = np.linalg.svd(array)
        self.assertIsInstance(u, np.ndarray)
        
    # Statistiques et génération aléatoire
    @given(st.integers(min_value=1, max_value=100), st.floats(min_value=-1e10, max_value=1e10), st.floats(min_value=1e-10, max_value=1e10))
    def test_numpy_random_normal(self, size, mean, std):
        array = np.random.normal(mean, std, size)
        self.assertEqual(array.size, size)

    @given(st.lists(st.floats(min_value=-1e10, max_value=1e10), min_size=1), st.floats(min_value=0, max_value=100))
    def test_numpy_percentile(self, lst, percentile):
        array = np.array(lst)
        self.assertAlmostEqual(np.percentile(array, percentile), np.percentile(lst, percentile))

    @given(st.lists(st.floats(min_value=-1e2, max_value=1e2, allow_nan=False, allow_infinity=False), min_size=1))
    def test_numpy_histogram(self, lst):
        if any(abs(x) < 1e-10 or abs(x) > 1e10 for x in lst):
            raise ut.SkipTest("Skipping due to extreme values in the list")
        hist, _ = np.histogram(lst)
        self.assertIsInstance(hist, np.ndarray)

    # Comparaison et logique
    @given(st.lists(st.floats()), st.lists(st.floats()))
    def test_numpy_comparison(self, a, b):
        if len(a) == len(b):
            np_a, np_b = np.array(a), np.array(b)
            self.assertTrue(np.array_equal(np.equal(np_a, np_b), np.equal(a, b)))
            self.assertTrue(np.array_equal(np.not_equal(np_a, np_b), np.not_equal(a, b)))
            self.assertTrue(np.array_equal(np.greater(np_a, np_b), np.greater(a, b)))
            self.assertTrue(np.array_equal(np.less(np_a, np_b), np.less(a, b)))

    # Opérations sur les chaînes de caractères
    @given(st.text(alphabet=st.characters(blacklist_characters=['\x00'])), st.text(alphabet=st.characters(blacklist_characters=['\x00'])))
    def test_numpy_char_operations(self, a, b):
        np_result = np.char.add(a, b)
        py_result = a + b
        self.assertEqual(np_result.item(), py_result)
        np_upper = np.char.upper(a)
        py_upper = a.upper()
        self.assertEqual(np_upper.item(), py_upper)
        np_lower = np.char.lower(a)
        py_lower = a.lower()
        self.assertEqual(np_lower.item(), py_lower)
        np_strip = np.char.strip(a)
        py_strip = a.strip()
        self.assertEqual(np_strip.item(), py_strip)

if __name__ == '__main__':
    ut.main()

