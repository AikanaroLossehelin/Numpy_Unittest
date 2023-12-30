# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 12:20:34 2023

@author: aikan

Installer chaque version de NumPy dans un environnement virtuel séparé.
Activer chaque environnement et localiser le répertoire d'installation de NumPy.
Exécuter versioning.py

Liste des versions de Numpy :
https://numpy.org/news/#releases
"""
import ast
import os
import difflib

###########################################################################################
#
# COMPARAISON DES SCRIPTS ENTRE VERSIONS
#
###########################################################################################

def read_file_contents(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def compare_files(file_path_v1, file_path_v2):
    old_code = read_file_contents(file_path_v2)
    new_code = read_file_contents(file_path_v1)

    d = difflib.Differ()
    return list(d.compare(old_code.splitlines(), new_code.splitlines()))

def compare_versions(directory_v1, directory_v2):
    diffs = {}

    for root, dirs, files in os.walk(directory_v1):
        for file in files:
            if file.endswith('.py'):
                file_path_v1 = os.path.join(root, file)
                file_path_v2 = file_path_v1.replace(directory_v1, directory_v2)

                if os.path.exists(file_path_v2):
                    diff = compare_files(file_path_v1, file_path_v2)
                    if diff:
                        diffs[file] = diff
    return diffs


###########################################################################################
#
# ANALYSE DU CODE ET DES FONCTIONNALITES
#
###########################################################################################

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

if __name__ == "__main__":

    # Récupération des chemins d'accès
    with open('envpath.txt', 'r') as file:
        lines = file.readlines()

    numpy_dir_v1 = lines[0].strip()[2:-2]
    numpy_dir_v2 = lines[1].strip()[2:-2]

    changes = compare_versions(numpy_dir_v1, numpy_dir_v2)

    # Création du fichier de comparaison des scripts
    with open('txt_compare.txt', 'w', encoding='utf-8') as out_file:
        for file, diff in changes.items():
            out_file.write(f"Changes in {file}:\n")
            out_file.write('\n'.join(diff))
            out_file.write("\n\n")

    # Création des deux fichiers d'analyse des scripts
    analyze_package(numpy_dir_v1, 'numpy_v1_analysis.txt')
    analyze_package(numpy_dir_v2, 'numpy_v2_analysis.txt')
