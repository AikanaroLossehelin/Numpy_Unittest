# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 12:20:34 2023

@author: aikan

Installer chaque version de NumPy dans un environnement virtuel séparé.
Activer chaque environnement et localiser le répertoire d'installation de NumPy.
Exécuter analyze_package sur chaque répertoire.

virtualenv numpy_v1
virtualenv numpy_v2

https://numpy.org/news/#releases

Pour chaque environnement (e.g. numpy_v1) :
    
numpy_v1\Scripts\activate
pip install numpy==[version_1]
python -c "import numpy; print(numpy.__path__)"
deactivate

"""
import ast
import os

def analyze_code(code, file_path, output_file):
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        with open(output_file, 'a') as out_file:
            out_file.write(f"SyntaxError in file {file_path}: {e}\n")
        return

    with open(output_file, 'a') as out_file:
        out_file.write(f"Analyzing {file_path}\n")
        for node in ast.walk(tree):
            out_file.write(f"{type(node).__name__}\n")

def analyze_file(file_path, output_file):
    with open(file_path, 'r', encoding='utf-8') as file:
        code = file.read()
    analyze_code(code, file_path, output_file)

def analyze_package(directory, output_file):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                analyze_file(file_path, output_file)

numpy_dir_v1 = 'C:\\Documents\\MINES ST-Etienne\\2023-2024\\Cours Dauphine\\POO\\Unittest_local\\numpy_v1\\Lib\\site-packages\\numpy'
numpy_dir_v2 = 'C:\\Documents\\MINES ST-Etienne\\2023-2024\\Cours Dauphine\\POO\\Unittest_local\\numpy_v2\\Lib\\site-packages\\numpy'

analyze_package(numpy_dir_v1, 'numpy_v1_analysis.txt')
analyze_package(numpy_dir_v2, 'numpy_v2_analysis.txt')