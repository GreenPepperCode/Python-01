# La story 1 : Type et variables (Python)

## Contexte
Dans le cadre d’apprentissage d’un nouveau langage de programmation, on va se familiariser avec le concept de variables, notion et leurs différents types ainsi que la conversion d’un type à un autre. Apprendre les premiers principes algorithmiques comme saisir une valeur à partir du clavier, affectation des variables, affichages du résultat, opérations arithmétiques sur des variables et comment écrire des commentaires du Genre # c’est un commentaire.

## Mot clé (= notion à apprendre)
- **Type :** Désigne la nature des données (comme int, str, float). Similaire à JavaScript, bien que Python soit plus strict sur les conversions de type.
- **Variables :** Conteneurs pour stocker des données. En Python, typage dynamique comme en JavaScript.
- **Constante :** Une variable dont la valeur ne change pas. Python n'a pas de mot-clé spécifique pour les constantes, mais par convention, on utilise des majuscules (ex : CONSTANT).
- **Algorithme :** Une procédure ou une formule pour résoudre un problème. Le concept est identique dans tous les langages de programmation.
- **Opérations :** Actions mathématiques ou logiques sur des variables. Les opérateurs en Python sont similaires à JavaScript.
- **Conversion du type :** Changer un type de données en un autre (ex : int en str). En Python, utilisez des fonctions comme int(), str(), similaire à JavaScript.
- **Backend :** Partie d'une application traitant la logique, la base de données, etc. En Python, frameworks comme Django ou Flask.
- **Frontend :** Partie de l'application que les utilisateurs voient (interface). Python n'est pas typiquement utilisé pour le frontend.
- **Affectation :** Assigner une valeur à une variable. En Python, utilisez = comme en JavaScript.
- **Type de variables :** Réfère aux différents types de données (comme list, dict en Python).
- **Booléens :** Type de données vrai/faux (True/False en Python).
- **Float :** Nombre à virgule flottante.
- **Integer :** Nombre entier.
- **String :** Séquence de caractères.
- **(Hello World) :** Programme de base affichant "Hello World".
- **Concaténation :** Joindre des chaînes de caractères. Utilisez + en Python.
- **Commentaires :** Notes dans le code ignorées lors de l'exécution. Utilisez # pour un commentaire en ligne en Python.
- **Règles de nommages des variables :** Conventions pour nommer les variables. Python utilise le snake_case par convention.
- **Portée des variables :** Où une variable est accessible. Similaire à JavaScript (global, local).
- **Local variable :** Variable accessible uniquement dans son contexte.
- **Global variable :** Variable accessible partout dans le code.
- **Modulo :** Opérateur pour le reste de la division (% en Python).
- **Les adresses mémoires :** Emplacement de stockage des données en mémoire.
- **Pointeurs :** Python n'utilise pas de pointeurs de la même manière que les langages comme C.
- **Script :** Un fichier de code exécutable.
- **Type primitif :** Types de base comme int, float, bool en Python.
- **Virgule flottante :** Format pour représenter des nombres réels.
- **Mantisse :** Partie du nombre en virgule flottante représentant sa précision.
- **Exposant :** Partie d'un nombre en virgule flottante indiquant l'ordre de grandeur.

## Problématique
- Comment effectuer la conversion d’un type à un autre ?
- Comment afficher, stocker, manipuler les variables ?
- Comment utiliser dans Jupyter Notebook (Anaconda) ?

## Hypothèses Vrai-Faux
1. Patrick : Une valeur peut contenir plusieurs variables. Faux. Une valeur est assignée à une variable, mais une seule valeur peut être assignée à une variable à la fois.
2. Salah : Variable peut être un tableau. Vrai. En Python, une variable peut contenir différents types de données, y compris un tableau (liste).
3. Y a une différence entre une valeur vide et nul. Vrai. En Python, une valeur vide (comme une liste vide []) est différente de None (équivalent de null).
4. Rafael : On peut convertir toutes les variables. Faux. Certaines conversions ne sont pas possibles si elles ne sont pas logiquement cohérentes (comme convertir une chaîne de texte non numérique en nombre).
5. Thibaut : Il est possible de stocker int() dans un str(). Vrai. Vous pouvez convertir un entier en chaîne de caractères en Python.
6. Alexis : Une variable peut être vide. Vrai. Une variable peut contenir une valeur vide, comme une liste vide ou une chaîne vide.
7. Hassan : Une variable peut contenir deux valeurs en même temps. Faux. Une variable ne peut contenir qu'une seule valeur à la fois, mais cette valeur peut être un ensemble de données, comme une liste.
8. Alexandre : Une même variable peut être de plusieurs types. Faux. Une variable ne peut avoir qu'un seul type à la fois, mais en Python, le type d'une variable peut changer.
9. Ahmed : Une variable booléenne peut prendre uniquement une des deux. Vrai. Les booléens sont soit True soit False.
10. Munkherdene : N'y a pas de code sans variables. Faux. Il est possible d'écrire du code sans déclarer des variables, bien que ce soit rare.
11. Bart : Python est orienté objets. Vrai. Python supporte la programmation orientée objet.
12. L’ensemble des concepts présent dans la story ne sont pas suffisants pour construire un langage Turing complet. Faux. Les concepts abordés dans la story, tels que les types, les variables, les opérations, etc., sont fondamentaux en programmation et, bien qu'ils ne couvrent pas tous les aspects d'un langage de programmation, ils font partie des éléments essentiels qui contribuent à la construction d'un langage Turing complet comme Python.
13. Paul : Une variable prend le type de sa valeur. Vrai. En Python, le type d'une variable est déterminé par la valeur qui lui est assignée.
14. Hadjer : En gros dans python y a 2 types de grandes familles de variables, les globales et les locales. Faux. Python a plusieurs types de données (comme int, str, list, etc.). La distinction entre variables globales et locales concerne leur portée dans le code, pas leur type de données. Les variables globales sont accessibles dans tout le script, tandis que les variables locales sont limitées à leur contexte, comme une fonction.
15. Philippe : On peut appeler les variables en dehors des scripts. Faux. Les variables doivent être définies dans le script ou importées pour être utilisées.


## Plan d’action
- Explorer les ressources
- Définir les mots clés
- Vérifier les hypothèses
- Faire les exos
- S’entrainer sur Jupyter
- Tableau types de variables
- RER

## Tableau des Types de Variables en Python
| Type de Variable | Description                             | Exemple            |
|------------------|-----------------------------------------|--------------------|
| int              | Nombre entier                           | `5`, `-3`, `42`    |
| float            | Nombre à virgule flottante              | `3.14`, `-0.001`   |
| str              | Chaîne de caractères                    | `'hello'`, `"A"`   |
| bool             | Valeur booléenne (Vrai ou Faux)         | `True`, `False`    |
| list             | Liste ordonnée et modifiable            | `[1, 2, 3]`        |
| tuple            | Liste ordonnée et non modifiable        | `(1, 2, 3)`        |
| set              | Ensemble non ordonné et non indexé      | `{1, 2, 3}`        |
| dict             | Collection de paires clé-valeur         | `{'a': 1, 'b': 2}` |
