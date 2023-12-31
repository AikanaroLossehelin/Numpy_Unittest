# **Numpy unittest**

Ce document traite de l'automatisation des tests unitaires pour la bibliothèque **NumPy** et de la comparaison entre les différentes versions.

## **Sommaire**
- [**Numpy unittest**](#numpy-unittest)
  - [**Sommaire**](#sommaire)
  - [**1. Tests et rapports des versions**](#1-tests-et-rapports-des-versions)
    - [**Tests unitaires**](#tests-unitaires)
    - [**Rapports de couverture**](#rapports-de-couverture)
  - [**2. Comparaison et analyse des versions**](#2-comparaison-et-analyse-des-versions)
    - [**Analyse des scripts**](#analyse-des-scripts)
    - [**Comparaison des scripts**](#comparaison-des-scripts)
  - [**3. Installation et génération des rapports**](#3-installation-et-génération-des-rapports)
- [**Annexe : Liste des fonctions testées**](#annexe--liste-des-fonctions-testées)
- [**Annexe : Création du rapport de couverture**](#annexe--création-du-rapport-de-couverture)
- [**Annexe : Création d'environnements virtuels**](#annexe--création-denvironnements-virtuels)


## **1. Tests et rapports des versions**

Dans cette partie nous abordons le programme **__init __.py** et l'étude de sa couverture.

### **Tests unitaires**

Dans un premier temps, notre travail s'est penché autour de la génération de tests unitaires pour la bibliothèque **NumPy**.  
Nous avons donc débuté ceci en identifiant les fonctions de la bibliothèque **NumPy** qui nous paraissaient intéressantes à tester (cf. [Annexe : Liste des fonctions testées](#liste-des-fonctions-testées)). Une fois la liste établie, il s'est agi de concevoir une classe fille - nommée *TestNumpyFunctions* - de la classe *TestCase* disponible dans la bibliothèque unittest.  
Une fois notre classe de test construite, nous avons rédigé des tests pour les différentes fonctions de la bibliothèque **NumPy** qui comparaient les résultats entre eux à l'aide des fonctions *assertEqual*, *assertTrue*, etc.

Ensuite, nous nous sommes penchés sur l'automatisation de ces tests unitaires. Et pour cela, nous nous sommes aidés de la bibliothèque **Hypothesis** permettant de générer des listes de données variées en type (str, int, float, etc.) comme en valeurs (valeurs négatives infinies, valeurs nulles, etc.) Alors, au moyen de la méthode *given* de la bibliothèque nous avons pu définir des jeux de données pour chacune de nos méthodes de tests. Ainsi, notre classe de test est munie d'une génération automatique et aléatoire de données de test parmi des échantillons définis de façon adaptée au bon fonctionnement des fonctions du package **NumPy** pour la version **1.26.2**. Par conséquent, aucun message d'erreur ni même d'avertissement n'est censé être généré lors de l'exécution de notre fonction pour la version en question.  
En outre, il est important de noter que notre choix implique de devoir réadapter le code à chaque nouvelle version de Numpy si l'on souhaite conserver une comparaison valable pour la dernière version en date.

Enfin, afin de prévenir certains changements qui auraient pu advenir dans de précédentes versions de **NumPy** ou afin d'aider à l'adaptation des jeux de test à l'avenir, nous avons programmé la génération de messages d'erreur dans certaines fonctions de tests. En effet, celles-ci ont pour but d'avertir l'utilisateur sur les raisons éventuelles d'erreurs ou de messages d'avertissement lors de l'exécution du programme ou de sa mise à jour pour des versions différentes de la nôtre. Ainsi, nous espérons que ces fonctionnalités aideront les éventuels contributeurs à la mise à jour de notre script.


### **Rapports de couverture**

Dans un second temps, nous avons produit un rapport de couverture de notre code afin de renseigner l'utilisateur sur l'ensemble des résultats des tests exécutés ainsi que sur la bonne exécution de nos lignes de code.  
Pour cela, nous avons utilisé le script **coverage.py** (cf. [Annexe : Création du rapport de couverture](#création-du-rapport-de-couverture)). Celui-ci permet de générer directement des rapports de couverture indiquant le taux de requêtes effectuées, échouées et manquées.  
En outre, il permet d'obtenir de précieux renseignements sur les éventuelles requêtes manquées lors de l'exécution. Mais il faut toutefois noter qu'il enregistre également les requêtes non exécutées pour cause d'absence de cas (e.g. une requête générant un message d'erreur ne sera pas exécutée si l'erreur ne se présente pas et donc sera comptabilisée parmi les requêtes manquées). Malgré cela et en l'absence d'une méthode de distinction des requêtes d'erreur lors de la couverture, nous préférons les conserver comme telles dans notre rapport étant donné leur utilité au débuggage et à la mise à jour de notre code.

**Nb :** A la date du 30/12/23, le rapport de couverture du programme **__init __.py** indique 182 requêtes couvertes dont 7 manquées (aux lignes 161, 167, 180, 188, 207-208, 239), soit un taux de couverture de 96% mais qui correspond à 100% de bon fonctionnement étant données la raison des lignes manquées.


## **2. Comparaison et analyse des versions**

Après la réalisation de nos tests unitaires et de leur automatisation, nous nous sommes penchés sur la comparaison et l'analyse des scripts entre différentes versions à travers le script **versioning.py**.  
Il est à noter qu'afin de comparer différentes versions d'une bibliothèque, nous recommandons de créer des environnements virtuels contenant chacun une version de ladite bibliothèque. Nous recommandons aux lecteurs de se référer à l'[annexe](#création-denvironnements-virtuels) correspondant pour la création des environnements virtuels dédiés à **NumPy**.

### **Analyse des scripts**

Tout d'abord, nous nous sommes intéressés à l'analyse fonctionnelle de notre code en comparant les types de requêtes effectuées ligne à ligne dans chacun des scripts de la bibliothèque **NumPy**.  
Alors, au moyen de trois fonctions (*analyze_code*, *analyze_file*, *analyze_package*), nous pouvons générer l'analyse des requêtes telle que stipulée pour une version du module étudié à l'aide de son adresse répertoire.  
Cette fonctionnalité nous a notamment intéressé car elle permet une analyse statistique des changements de type de requêtes entre deux versions ainsi qu'une observation purement informatique des actions effectuées dans chacun des scripts de chaque version.

### **Comparaison des scripts**

Toutefois, n'ayant pas trouvé davantage d'interprétation plus riche à notre analyse du fait de sa naïveté, nous avons décidé de nous tourner vers une comparaison plus précise des scripts des différentes versions.  
Nous nous sommes alors appuyés sur le module **Difflib** pour effectuer cette comparaison textuelle entre deux versions de la bibliothèque étudiée. En effet, à l'aide des trois fonctions programmées (*read_file_contents*, *compare_files*, *compare_versions*) nous parvenons à rendre un rapport détaillant toutes les différences entre deux versions du module étudié en indiquant notamment les ajouts et les suppressions ou encore les lignes modifiées.

Il est utile de noter que nos deux fonctions décomposant l'action d'analyse et de comparaison à différentes échelles de nos librairies, il devrait être relativement aisé d'ajouter de nouvelles fonctionnalités à ces différents niveaux. En outre, ces fonctionnalités peuvent également être employées pour la comparaison de divers modules autres que **NumpPy**.

**Nb :** Nous précisons que dans notre fichier **versioning.py**, la localisation desdits modules se fait via un fichier envpath.txt - dans notre version actuelle.

## **3. Installation et génération des rapports**

Afin de simplifier la tâche aux nouveaux utilisateurs et de permettre une exécution groupée de l'ensemble de nos rapports générés par les scripts précédemment présentés, nous accompagnons notre code d'un fichier batch **numpy_unittest.bat**.    

Tout d'abord, notre script batch vérifie la présence du fichier **coverage.py** ainsi que de la présence par défaut des environnements virtuels nommés par défaut *numpy_v1*, *numpy_v2*.
Si ceux-ci manquent dans le répertoire où s'exécute le script, ils seront respectivement téléchargés et crées. Mais il est important de noter qu'afin que le script exécute correctement le fichier **__init __.py**, il est nécessaire que les environnements virtuels soient dotés de la bibliothèque **Hypothesis**. Par conséquent, **notre fichier batch effectue l'installation dudit module dans la même boucle que la création des environnements virtuels**.  
C'est pourquoi, nous recommandons aux utilisateurs de supprimer les environnements virtuels dédiés à **NumpPy** s'ils venaient à ne pas être dotés du module **Hypothesis** ou bien de l'installer en amont de l'exécution du script.
En outre, un fichier **envpath.txt** sera créé lors de la création desdits environnements avec l'adresse vers les répertoires **NumPy** de chacune de ces versions.

Ensuite, ce fichier s'occupe donc à partir d'environnements virtuels nommés par défaut *numpy_v1*, *numpy_v2* d'exécuter les codes des fichiers **__init __.py** et **versioning.py** puis de stocker dans le cas du premier, le rapport de couverture dans un fichier nommé **report.txt**.  
Alors, l'utilisateur pourra s'assurer de la bonne exécution du script batch en vérifiant la présence des documents **report.txt**, **txt_compare.txt**, **numpy_v1_analysis.txt** et **numpy_v2_analysis.txt**.  
En outre, nous avons fait le choix dans notre fichier batch de conserver les précédents rapports de couverture générés par son exécution afin de permettre aux utilisateurs de comparer leurs résultats et de garder un historique de leurs tests. L'utilisateur est donc libre de supprimer tout ou partie du fichier **report.txt** au cours de son travail.

Enfin, il est important de noter plusieurs éléments nécessaires au bon emploi de notre script.   
Premièrement, celui-ci requiert la connexion entre le terminal utilisé et la version de Python utilisée. Nous conseillons d'utiliser le Powershell d'Anaconda afin de simplifier ce travail.  
Deuxièmement, les versions de **NumPy** installées dans les environnement virtuels programmés par défaut sont respectivement pour les environnements *numpy_v1*, *numpy_v2*, les versions **1.24.0** et **1.23.0**. L'utilisateur devra donc se montrer attentif à leur bonne modification s'il souhaite en tester d'autres.  
Finalement, nous accompagnons notre script batch d'une version pour système Unix nommée **numpy_unittest_u.sh**. Toutefois, manquant des outils et de la connaissance pour l'adapter parfaitement à un tel environnement, le script n'est pas pleinement opérationnel. Nous laissons le soin aux utilisateurs confirmés d'adapter et de corriger ce script.

**Nb :** Nous laissons à disposition les versions texte de nos scripts batch et bash afin de faciliter la prise en main et la modification de ceux-ci.

<a id="liste-des-fonctions-testées"></a>

# **Annexe : Liste des fonctions testées**

Dans cette annexe, nous présentons la liste de toutes les fonctions du module numpy qui sont testées par le fichier *__init __.py*

- **Création d'Arrays:**

*numpy.array* : Crée un array à partir d'une liste ou d'un tuple.  
*numpy.zeros* : Crée un array rempli de zéros.  
*numpy.ones* : Crée un array rempli de uns.  
*numpy.arange* : Crée un array avec une séquence de nombres.  
*numpy.linspace* : Crée un array de valeurs espacées uniformément.  

- **Opérations Mathématiques:**

*numpy.add, numpy.subtract, numpy.multiply, numpy.divide* : Opérations arithmétiques de base.  
*numpy.sqrt* : Racine carrée.  
*numpy.exp* : Exponentielle.  
*numpy.sin, numpy.cos, numpy.tan* : Fonctions trigonométriques.  
*numpy.log/numpy.log10* : Logarithmes naturel et décimal.  
*numpy.power* : Élévation à une puissance.  
*numpy.hypot* : Calculer l'hypoténuse de nombres.  

- **Manipulation d'Arrays:**

numpy.reshape : Modifie la forme d'un array.  
numpy.concatenate : Concatène des arrays.  
numpy.split : Divise un array en plusieurs sous-arrays.  
numpy.transpose : Transpose un array.   
numpy.ravel : Aplatir un tableau en 1D.  
numpy.expand_dims : Ajouter une nouvelle dimension.  
numpy.squeeze : Supprimer les axes de longueur un.  

- **Statistiques et Aggrégations:**

numpy.mean : Moyenne.  
numpy.median : Médiane.  
numpy.std : Écart type.  
numpy.sum : Somme des éléments.   
numpy.max/numpy.min : Trouver le maximum/minimum dans un tableau.  
numpy.argmax/numpy.argmin : Trouver les indices du maximum/minimum.  
numpy.var : Calculer la variance.  
numpy.random.normal : Générer des données normalement distribuées.  
numpy.percentile : Calculer le percentile.  
numpy.histogram : Calculer l'histogramme d'un jeu de données.  

- **Algèbre Linéaire:**

numpy.linalg.inv : Inversion de matrice.  
numpy.linalg.det : Déterminant d'une matrice.  
numpy.dot : Produit scalaire ou produit matriciel.   
numpy.trace : Calculer la trace d'une matrice.  
numpy.linalg.eig : Calculer les valeurs et vecteurs propres.  
numpy.linalg.svd : Décomposition en valeurs singulières.  

- **Comparaison et logique:**

numpy.equal/numpy.not_equal : Tests d'égalité ou de différence.  
numpy.greater/numpy.less : Comparaison supérieure ou inférieure.  
numpy.logical_and/numpy.logical_or : Opérations logiques.  

- **Opérations sur les chaînes de caractères:**

numpy.char.add : Concaténer des chaînes de caractères.  
numpy.char.upper/numpy.char.lower : Convertir en majuscules ou minuscules.  
numpy.char.strip : Supprimer les espaces de début et de fin.  

<a id="création-du-rapport-de-couverture"></a>

# **Annexe : Création du rapport de couverture**

Nous joignons ci-dessous une brève explication du fichier **coverage.py**.

Celui-ci s'emploie via un invité de commande relié à Python et sur un fichier *.py* important le module unittest.  
On commence par exécuter notre fichier à l'aide de la commande suivante :
```
coverage run -m unittest <nom_du_fichier_sans_extension>
```

Nous obtenons alors un retour sous la forme d'une succession de messages d'avertissements et de bandereaux d'échec ("Fail") si de tels cas se présentent lors de nos tests. Le tout suivi d'un message de confirmation d'arrêt ("Ok").  
On peut ensuite résumer l'exécution dans un tableau de la façon suivante :
```
coverage report -m
```

**Nb :** Le paramètre d'option "-m" permet d'obtenir le détail des lignes manquées au cours de l'exécution. Ainsi, nous préférons son utilisation afin de simplifier le débuggage ou la bonne vérification de notre scripts.

Cette commande fournit alors un tableau synthétique de notre couverture de la forme suivante :
```
Name          Stmts   Miss  Cover   Missing
-------------------------------------------
__init__.py     182      7    96%   161, 167, 180, 188, 207-208, 239
-------------------------------------------
TOTAL           182      7    96%
```
Nous pouvons alors constater dans notre exemple que nous avons lu 182 requêtes, que 7 ont été ignorées ce qui nous fait une couverture de 96% de notre code et que nous n'avons pas exécuté les lignes 161, 167, 180, 188, 207-208 et 239.

Enfin, pour des utilisateurs désirant déposer leur rapport sur une page html d'un serveur ou de l'y ajouter, nous précisons que la commande suivante permet de générer notre rapport en version html :

```
coverage html
```

<a id="création-denvironnements-virtuels"></a>

# **Annexe : Création d'environnements virtuels**

Pour utiliser **versioning.py**, la création d'environnements virtuels contenant le module **NumPy** est vivement recommandée. De ce fait, nous présentons succinctement dans cette annexe comment procéder.

Tout d'abord, nous conseillons l'emploi de la commande *virtualenv* pour la création de tels environnements comme suit :

```
virtualenv <nom_environnement_virtuel>
```

Une fois l'environnement créé, il est nécessaire de l'activer pour que notre machine établisse les installations au bon endroit. Nous utilisons la commande suivante :

```
<nom_environnement_virtuel>\Scripts\activate
```

Il ne reste ensuite plus qu'à installer les bibliothèques aux versions souhaitées avec la commande suivante :

```
pip install <nom_module>==<version>
```

Puis, nous désactivons l'environnement une fois que nous avons fini d'y travailler pour revenir à nos autres tâches ou environnements avec la commande suivante :

```
deactivate
```





