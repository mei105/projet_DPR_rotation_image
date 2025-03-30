# Le projet sur la rotation d'une image
<i>Par APET Vlad, Mathieu et Gaël</i> - Terminale<br><br>

Ce projet présente un programme (console Python) qui permet de tourner une image choisie d'un quart de tour vers la droite ou vers la gauche (selon son choix)

Il a été réalisé avec les bibliothèques Pillow, pygame ainsi que tkinter.

# Précisions préalables
<ul>
  <li>Les réponses aux questions de l'énoncé du projet 1 se trouvent directement dans le fichier <code>rotation.py</code> et sont indiquées par les commentaires.</li>
  <li>Vous ne pouvez retourner votre image qu'une seule fois.</li>
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
  <li>Vous devez également posséder la bibliothèque Pillow. Pour la télécharger, utiliser la commande <code>pip install Pillow</code> Si vous rencontrez des problèmes, consultez la documentation de Pillow (Source : https://pillow.readthedocs.io/en/stable/).</li>
  <li>Idem pour la bibliothèque tkinter</li>
  <li>Lancer/Exécuter le fichier <code>rotation.py</code><br></li>
  <li>Choisissez votre image à tourner et le type de rotation souhaité.</li>
  <li>Observer le résultat à travers la fenêtre pygame qui vient de s'ouvrir pour vous.</li>
</ol><br>

# Limitations éventuelles
<p>On peut en citer quelques-unes :</p>
<ol>
  <li>Votre image doit être <b>carrée</b> (côtés égaux) et chaque côté correspond à la <b>puissance de 2</b>. Sinon, si vous le souhaitez, on rogne votre image et on effectue une rotation.</li>
  <li>La taille de votre image doit être de 32x32 (au minimum) et ne depassant pas 800x800 (ici la taille en pixels, bien entendu)</li>
  <li>Votre image doit oobligatoirement être de format .png, .jpeg, .jpg</li>
  <li>Fournissez des informations correctes, car toute saisie érronée peut arrêter votre démarche et il faudra recommencer.</li>
</ol><br>

# Améliorations envisageables 
<ol>
  <li>Si l'énoncé ne le nécessitait pas, on aurait pu ne pas rogner l'imager et la tourner par la méthode de force brute (pixel par pixel) et non pas selon la méthode DPR.</li>
  <li>C'est avec plaisir qu'on aurait pu également aller encore plus loin et sortir du cadre de l'énoncé, en développant une interface pygame (et non pas la console), <br>en faisant bien sûr attention à la taille des boutons, ainsi qu'à leur placement et celui de l'image, par exemple. <br>(Mais ceci est envisageable que lorsque les coéquipiers <b>principaux</b> ne passent pas déjà énormement de concours et peuvent donc réaliser de tels ajouts)</li>
</ol><br>
