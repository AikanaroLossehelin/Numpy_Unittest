# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 17:56:59 2023

@author: aikan
"""

import unittest as ut
import numpy as np
import sys

def generate_test_data():
    test_cases = []

    # Cas typiques
    test_cases.append(([1, 2, 3], "Simple list"))  # Liste simple
    test_cases.append(([1.1, 2.2, 3.3], "List of floats"))  # Liste de flottants
    test_cases.append(([(1,2), (3,4)], "List of tuples"))  # Liste de tuples
    test_cases.append(([], "Empty list"))  # Liste vide

    # Cas avec différents types de données
    test_cases.append((['a', 'b', 'c'], "List of strings"))  # Liste de chaînes
    test_cases.append(([True, False, True], "List of booleans"))  # Liste de booléens

    # Cas limites
    test_cases.append((list(range(1000000)), "Large list"))  # Très grande liste
    test_cases.append(([[1, 2], [3, 4, 5]], "Jagged array"))  # Array irrégulier

    # Cas de données complexes ou spéciaux
    test_cases.append((np.zeros((2, 3)), "2D array of zeros"))  # Array 2D de zéros
    test_cases.append((1 + 2j, "Complex number"))  # Nombre complexe

    # Cas extrêmes
    test_cases.append((sys.maxsize, "Maximum integer size"))  # Taille max d'un entier
    test_cases.append((np.inf, "Infinity"))  # Infini
    test_cases.append((np.nan, "NaN"))  # Not a Number

    return test_cases

def test_numpy_array():
    test_cases = generate_test_data()

    for data, description in test_cases:
        try:
            array = np.array(data)
            print(f"Test passed for: {description}")
            print(f"Array: {array}\n")
        except Exception as e:
            print(f"Test failed for: {description}")
            print(f"Error: {e}\n")

# Exécuter les tests
test_numpy_array()


class TestNumpyFunctions(ut.TestCase):

    def test_numpy_array(self):
        # Cas typiques
        self.assertTrue(np.array_equal(np.array([1, 2, 3]), np.array([1, 2, 3])))
        # Cas limites et d'erreur...

    def test_numpy_zeros(self):
        self.assertTrue(np.array_equal(np.zeros(3), np.array([0, 0, 0])))
        # Autres cas...

    def test_numpy_ones(self):
        self.assertTrue(np.array_equal(np.ones(3), np.array([1, 1, 1])))
        # Autres cas...

    def test_numpy_arange(self):
        self.assertTrue(np.array_equal(np.arange(3), np.array([0, 1, 2])))
        # Autres cas...

    def test_numpy_linspace(self):
        self.assertTrue(np.array_equal(np.linspace(1, 3, 3), np.array([1, 2, 3])))
        # Autres cas...

    # Tests similaires pour les autres fonctions...

if __name__ == '__main__':
    ut.main()

