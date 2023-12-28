@echo off

REM Vérifier si coverage.py est installé
pip show coverage >nul 2>&1

REM Vérifier le code de sortie de la commande précédente
IF %ERRORLEVEL% NEQ 0 (
    echo coverage.py not found. Installation in progress...
    pip install coverage
    IF %ERRORLEVEL% NEQ 0 (
        echo Coverage.py installation failed.
        exit /b 1
    ) ELSE (
        echo coverage.py has been successfully installed.
    )
)

REM Initialiser une variable pour suivre la création des environnements
SET env_created=0

REM Boucle sur les deux environnements
FOR %%j IN (1 2) DO (
    REM Vérifier si l'environnement virtuel existe
    IF NOT EXIST numpy_v%%j (
        REM Environnement n'existe pas, le créer et installer NumPy
        virtualenv numpy_v%%j
        CALL numpy_v%%j\Scripts\activate

        REM Installer NumPy
        IF %%j == 1 (pip install numpy==1.24.0) ELSE (pip install numpy==1.23.0)

        REM Installer Hypothesis
        pip install hypothesis

        REM Afficher le chemin de NumPy et l'ajouter à envpath.txt
        python -c "import numpy; print(numpy.__path__)" >> envpath.txt

        REM Désactiver l'environnement
        deactivate

        REM Marquer que les environnements ont été créés
        SET env_created=1
    )
    IF %%j == 2 (
IF %env_created% == 1 (
    echo The numpy virtual environments have been added to the directory. > report.txt
)

FOR %%k IN (1 2) DO (
    CALL numpy_v%%k\Scripts\activate >> report.txt 2>>&1
    echo Activating numpy_v%%k environment and running tests... >> report.txt 2>>&1

    coverage run -m unittest __init__ > temp_results.txt 2>>&1
    coverage report -m >> report.txt
    echo.>> report.txt

    type temp_results.txt >> report.txt
    echo.>> report.txt
    del temp_results.txt

    deactivate >> report.txt 2>>&1
    IF %%k == 2 (python versioning.py)
))
)

REM Enregistrer un message si de nouveaux environnements ont été créés
IF %env_created% == 1 (
    echo The numpy virtual environments have been added to the directory. > report.txt
)

REM Exécuter les tests dans les environnements
FOR %%j IN (1 2) DO (
    REM Activer l'environnement
    CALL numpy_v%%j\Scripts\activate >> report.txt 2>>&1
    echo Activating numpy_v%%j environment and running tests... >> report.txt 2>>&1

    REM Exécuter les tests avec coverage et stocker temporairement les résultats
    coverage run -m unittest __init__ > temp_results.txt 2>>&1

    REM Ajouter le rapport de couverture au fichier report.txt
    coverage report -m >> report.txt
    echo.>> report.txt

    REM Ajouter les résultats des tests stockés temporairement à report.txt
    type temp_results.txt >> report.txt
    echo.>> report.txt

    REM Supprimer le fichier temporaire
    del temp_results.txt

    REM Désactiver l'environnement
    deactivate >> report.txt 2>>&1
    IF %%j == 2 (python versioning.py)
)