# Le projet sur le code morse
<i>Par APET Vlad, Mathieu et Gaël</i> - Terminale<br><br>

# Reste à faire :
1. Completer le fichier du tp avec tout ce qui a été fait jusqu'au moment présent. (pour que le prof puisse se repérer faciliment dans le fichier main.py)
2. Répondre à la question 2 (C'est O(n^2) décidément)
3. Vérifier la conformité aux exigeances de l'énoncé (pronote et tp)
4. Tester tout (y compris les cas limites)

# Précisions préalables
<ul>
  <li>Les réponses aux questions de l'énoncé du projet 1 se trouvent directement dans le fichier <code>main.py</code> et sont indiquées par les commentaires.</li>
</ul>

# Répartition des tâches & Lancement
<i>Vlad</i> s'est chargé :<br>
<ul>
  <li>De la construction de l'interface à travers la console.</li>
  <li>De la structure du projet, ainsi que du développement des fonctions (rotation gauche, vérification des images passées, etc...)</li>
  <li>L'amélioration de la documentation (README, commentaires, etc...)</li>
  <li>Divers tests de l'intégrité du projet</li>
</ul><br>

<i>Mathieu</i> s'est chargé de :<br>
<ul>
  <li>La documentation (fichier README, commentaires...)</li>
  <li>La rotation "brute" de l'image (celle qui consiste à "directement" tourner l'image pixel par pixel.)</li>
  <li>Divers tests (des rotations notamments)</li>
</ul><br>

<i>Gaël</i> s'est chargé de :<br>
<ul>
  <li>La documentation (commentaires...)</li>
  <li>Le développement de la fonction qui correspond à la rotation droite.</li>
  <li>Divers tests (des rotations et de l'interaction avec l'utilisateur.)</li>
</ul><br>


# Comment lancer le programme?
<ol>
  <li>Assurez vous d'avoir installé la bibliothèque "pygame". Si vous ne l'avez pas, tapez dans la console : <code>pip install pygame</code> (si vous n'y arrivez pas, consulter la vidéo suivante :  https://youtu.be/-z-bBY6YUVU)</li>
  <li>Lancer/Exécuter le fichier main.py<br></li>
  <li>Choisissez votre image à tourner et le type de rotation souhaité.</li>
  <li>Observer le résultat à travers la fenêtre pygame qui vient de s'ouvrir pour vous.</li>
</ol><br>

# Limitations éventuelles
<p>On peut en citer quelques-unes :</p>
<ol>
  <li>Votre image doit être <b>carrée</b> (côtés égaux) et dont chaque côté correspond à la <b>puissance de 2</b>. Sinon, si vous le souhaitez, on rogne votre image et on effectue une rotation.</li>
  <li>La taille de votre image ne doit pas depasser 1000x1000 (ici en pixels, bien entendu)</li>
  <li>Fournissez des informations correctes, car toute saisie érronée peut arrêter votre démarche et il faudra recommencer.</li>
</ol><br>

# Améliorations envisageables 
<ol>
  <li>On pourrait éventuellement ne pas rogner l'imager et la tourner </li>
  <li>C'est avec plaisir qu'on aurait pu aller encore plus loin que l'énoncé et développer une interface via la fenêtre pygame (et non pas la console), en faisant attention à la taille des boutons, ainsi qu'à leur placement et celui de l'image, par exemple.</li>
</ol><br>
