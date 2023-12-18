# Unittest

On s'intéresse à l'automatisation des tests unitaires pour la bibliothèque Numpy.

## Protocole

### Identification des fonctions à tester

**Sélectionner les fonctions à tester :** Identifiez les fonctions de la bibliothèque NumPy que vous souhaitez tester de manière automatisée. Concentrez-vous sur les fonctions critiques ou celles qui sont souvent utilisées dans votre code.

### Création des données de test

**Créer des jeux de données de test :** Générez des données d'entrée de test qui couvrent un large éventail de cas possibles. Cela peut inclure des tableaux NumPy avec différentes formes, types de données et valeurs. Vous pouvez également utiliser des générateurs de données aléatoires pour créer des entrées variées.

### Programmation des tests unitaires automatisés

**Écriver des tests unitaires automatisés :** Pour chaque fonction que vous souhaitez tester, écrivez des tests unitaires automatisés en utilisant un framework de test comme unittest, pytest, ou nose. Ces tests devraient inclure des assertions qui comparent les résultats attendus aux résultats réels de la fonction.

### Exécution des tests

**Exécuter les tests :** Exécutez vos tests unitaires automatisés pour vérifier que les fonctions NumPy se comportent comme prévu. Assurez-vous de vérifier les rapports de tests pour détecter les échecs et les erreurs.

### Extensions et approfondissement

**Utiliser des bibliothèques de génération de tests :** Il existe des bibliothèques et des outils qui peuvent vous aider à générer des tests automatiques pour NumPy. Par exemple, Hypothesis est une bibliothèque de génération de tests en Python qui peut générer automatiquement des données de test et des cas de test pour NumPy. Vous pouvez l'utiliser pour automatiser la génération de données d'entrée pour vos fonctions NumPy.

### Rapports de couverture

**Analyser les rapports de couverture de code :** Pour vous assurer que vos tests couvrent efficacement votre code NumPy, utilisez des outils de couverture de code comme coverage.py pour identifier les parties du code qui ne sont pas testées.

### Mise à jour des tests

**Maintenez vos tests à jour :** Assurez-vous de maintenir vos tests à jour à mesure que votre code évolue. Les tests unitaires automatisés sont un outil précieux pour garantir que les modifications du code ne cassent pas les fonctionnalités existantes.

## Liste des fonctions critiques à étudier

- **Création d'Arrays:**

numpy.array : Crée un array à partir d'une liste ou d'un tuple.  
numpy.zeros : Crée un array rempli de zéros.  
numpy.ones : Crée un array rempli de uns.  
numpy.arange : Crée un array avec une séquence de nombres.  
numpy.linspace : Crée un array de valeurs espacées uniformément.  

- **Opérations Mathématiques:**

numpy.add, numpy.subtract, numpy.multiply, numpy.divide : Opérations arithmétiques de base.  
numpy.sqrt : Racine carrée.  
numpy.exp : Exponentielle.  
numpy.sin, numpy.cos, numpy.tan : Fonctions trigonométriques.  

- **Manipulation d'Arrays:**

numpy.reshape : Modifie la forme d'un array.  
numpy.concatenate : Concatène des arrays.  
numpy.split : Divise un array en plusieurs sous-arrays.  
numpy.transpose : Transpose un array.  

- **Statistiques et Aggrégations:**

numpy.mean : Moyenne.  
numpy.median : Médiane.  
numpy.std : Écart type.  
numpy.sum : Somme des éléments.  

- **Algèbre Linéaire:**

numpy.linalg.inv : Inversion de matrice.  
numpy.linalg.det : Déterminant d'une matrice.  
numpy.dot : Produit scalaire ou produit matriciel.  

- **Indexation et Slicing:**  

Indexation avancée et slicing pour accéder et modifier des parties spécifiques d'un array.

- **Fonctions Universelles (ufuncs):**

Fonctions qui opèrent élément par élément sur des arrays.






