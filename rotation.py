import pygame
import tkinter as tk
from tkinter import filedialog
from pygame.locals import *
from PIL import Image
import math


def choisir_image():
    """Permet à l'utilisateur de choisir son image à tourner.

    :return: Le chemin qui mène à une image choisie. (de type str)
    """
    root = tk.Tk()
    # root.withdraw()  # Cacher la fenêtre principale de Tkinter
    file_path = filedialog.askopenfilename(filetypes=[("Images", "*.png;*.jpg;*.jpeg")])
    root.destroy()
    return file_path


def verification_taille(fichier_chemin):
    """Elle vérifie si l'image est carrée et si chaque côté est une puissance de 2.

    :param fichier_chemin: Le chemin qui mène à une image choisie. (de type str)
    :return: 2-tuple (condition, log2_cote) où condition est une valeur booléenne (de type bool)
    qui par True indique que la taille est correcte ou par False le cas contraire
    et où log2_cote est une valeur de la puissance de 2 du côté le plus petit (de type float)
    """
    condition = False
    with Image.open(fichier_chemin) as img:
        taille = img.size
        if taille[0] < 32 or taille[1] < 32:
            print("\nVotre image n'est pas suffisamment grande pour être retournable, voire visible."
                  " Essayez de fournir des images de taille supérieure à 32x32")
            pygame.quit()
            exit()
        if taille[0] > 800 or taille[1] > 800:
            print("\nVotre image est trop grande. Essayez de fournir une image de taille inférieure à 800x800")
            pygame.quit()
            exit()
        if taille[0] == taille[1]:
            log2_cote = math.log2(taille[0])
            # log2_cote sert à rogner l'image (si l'on veut la tourner
            # malgré le fait qu'elle ne respecte pas toutes les consignes)
            if float(math.floor(math.log2(taille[0]))) == math.log2(taille[0]):
                condition = True
                return condition, log2_cote
            else:
                return condition, log2_cote
        else:
            if taille[0] < taille[1]:
                log2_cote = math.log2(taille[0])
                return condition, log2_cote
            else:
                log2_cote = math.log2(taille[1])
                return condition, log2_cote


def numeric_input_verification(user_input):
    """Elle sert essentiellement à vérifier si l'utilisateur utilise que des nombres

    :param user_input: La saisie de l'utilisateur (de type str)
    :return: user_input converti en nombre entier (s'il ne présente que des nombres),
    sinon, on arrête le programme et affiche le message d'erreur dans la console.
    """
    if user_input.isnumeric():
        return int(user_input)
    else:
        print("ERROR. Nous ne pouvons pas accepter votre saisie,"
              "essayez de n'utiliser que deux nombre: 0 ou 1")
        pygame.quit()


class Main:

    def __init__(self):
        """ Affiche l'image choisie dans une fenêtre pygame
        et applique la méthode rotation_dpr().
        """
        # initialisation de pygame
        pygame.init()
        print("Bonjour !")
        user_choice = numeric_input_verification(input("\nCe programme vous permet de tourner une image "
                                                       "à votre choix, voulez-vous poursuivre ? "
                                                       "Saisissez 1 pour continuer ou 0 pour s'arrêter."))

        if user_choice == 1:
            sens_rotation = numeric_input_verification(input("\nQuelle rotation voulez-vous effectuer ? "
                                                             "(1 pour la rotation d'un quart de tour vers la droite, "
                                                             "0 pour la rotation gauche)"))
            pygame.time.wait(1000)
            if sens_rotation not in (0, 1):
                print("Saisie erronée. Veuillez recommencer.")
                pygame.quit()
                exit()
            user_choice = numeric_input_verification(input("\nMaintenant, veuillez choisir votre image. "
                                                           "Attention, seuls les formats .png, .jpeg "
                                                           "et .jpg sont acceptés \nVotre image doit avoir "
                                                           "une taille de 32x32 (minimum) et elle ne doit pas "
                                                           "dépasser la taille 800x800. Elle doit aussi être "
                                                           "(dans la mesure du possible) carrée"
                                                           "\nEnfin, sachez que chaque côté doit être "
                                                           "une puissance de 2..."
                                                           "Souhaitez-vous continuer ? "
                                                           "(1 pour continuer, 0 pour s'arrêter)"))
            if user_choice == 1:
                pygame.time.wait(1000)
                # affichage de l'image
                fichier_chemin = choisir_image()
                if fichier_chemin:
                    # On vérifie si la taille est correcte
                    # et on extrait la puissance de 2 la plus adaptée en fonction des cas.
                    taille_correcte, log2_cote = verification_taille(fichier_chemin)
                    if taille_correcte:
                        print("\nVotre rotation a été effectuée avec succès.")
                        self.window = pygame.display.set_mode((800, 800), DOUBLEBUF)
                        image = pygame.image.load(fichier_chemin)
                        self.window.blit(image, (0, 0))
                        pygame.display.update()
                        # rotation de l'image
                        self.rotation_dpr(0, 0, (2 ** int(log2_cote)) // 2, sens_rotation)

                        # maintien de la fenêtre
                        self.hold()
                    else:
                        user_choice = numeric_input_verification(
                            input("\nLa taille de votre image ne respecte pas toutes les consignes, "
                                  "mais on peut toujours la tourner à condition qu'elle soit rognée."
                                  "Voulez-vous continuer ? (tapez 1 pour oui, "
                                  "sinon tapez 0 ou tout autre caractère pour qu'on s'arrête.)"))
                        if user_choice == 1:
                            print("\nVotre image a été rognée et la rotation a été effectuée avec succès.")
                            self.window = pygame.display.set_mode((800, 800), DOUBLEBUF)
                            image = pygame.image.load(fichier_chemin)
                            # On rogne l'image...
                            self.window.fill((0, 0, 0))
                            pygame.display.update()
                            surface_rogne = self.window.subsurface((0, 0, (2 ** int(log2_cote)), (2 ** int(log2_cote))))
                            surface_rogne.blit(image, (0, 0))
                            pygame.display.update()
                            # rotation de l'image
                            self.rotation_dpr(0, 0, (2 ** int(log2_cote)) // 2, sens_rotation)

                            # maintien de la fenêtre
                            self.hold()
                        else:
                            print("\nMerci pour votre confiance, à bientôt !")
                            pygame.quit()
                            exit()
                else:
                    print("Aucune image choisie.")
                    pygame.quit()
                    exit()

            elif user_choice == 0:
                print("Merci de compter sur nos services.")
                pygame.quit()
            else:
                print("ERROR. Nous ne pouvons pas accepter votre saisie,"
                      "essayer de choisir entre 1 et 0 (sans espaces)")
                pygame.quit()
        elif user_choice == 0:
            print("Merci de compter sur nos services.")
            pygame.quit()
        else:
            print("ERROR. Nous ne pouvons pas accepter votre saisie,"
                  "essayer de choisir entre 1 et 0 (sans espaces)")
            pygame.quit()

    def rotation_dpr(self, x, y, t, sens):
        """Elle tourne l'image d'un quart de tour vers la droite ou bien vers la gauche.

        :param x: L'abscisse du tout premier pixel (coin supérieur gauche) (de type int)
        :param y: L'ordonnée du tout premier pixel (coin supérieur gauche) (de type int)
        :param t: La taille de l'image en question (largeur, hauteur) (de type tuple)
        :param sens: Le sens de rotation choisi par l'utilisateur (1 pour tourner à droite, à gauche : 1) (de type int)
        """

        if t > 1:
            self.rotation_dpr(x + t, y, t // 2, sens)
            self.rotation_dpr(x, y + t, t // 2, sens)
            self.rotation_dpr(x, y, t // 2, sens)
            self.rotation_dpr(x + t, y + t, t // 2, sens)
        if sens == 1:
            # Dans ce cas précis, on cherche à tourner l'image à droite.
            for j in range(x, x + t):
                for i in range(y, y + t):
                    # Algorithme qui change les pixels selon l'énoncé, d'ailleurs.
                    tl = self.window.get_at((i, j))
                    tr = self.window.get_at((i + t, j))
                    br = self.window.get_at((i + t, j + t))
                    bl = self.window.get_at((i, j + t))

                    self.window.set_at((i, j), bl)
                    self.window.set_at((i + t, j), tl)
                    self.window.set_at((i + t, j + t), tr)
                    self.window.set_at((i, j + t), br)
        elif sens == 0:
            # Dans cette condition, on cherche à tourner l'image à gauche.
            for i in range(x, x + t):
                for j in range(y, y + t):
                    # Algorithme qui change les pixels selon l'énoncé, d'ailleurs.
                    tl = self.window.get_at((i, j))
                    tr = self.window.get_at((i + t, j))
                    br = self.window.get_at((i + t, j + t))
                    bl = self.window.get_at((i, j + t))

                    self.window.set_at((i, j + t), tl)
                    self.window.set_at((i, j), tr)
                    self.window.set_at((i + t, j), br)
                    self.window.set_at((i + t, j + t), bl)

        # on fait cet appel systématiquement, car sinon
        # le système pygame risque de verrouiller la fenêtre
        # pendant la rotation !
        # C'est lié à la file d'attente des événements...
        pygame.event.pump()
        # mise à jour de l'affichage
        # (pour montrer comment les pixels se déplacent selon la méthode DPR)

        pygame.display.update()

    def hold(self):
        """Maintient la fenêtre ouverte jusqu'à sa fermeture ou la pression de la touche 'Echap'."""
        lock = True
        while lock:
            events_list = pygame.event.get()
            for event in events_list:
                if event.type == QUIT:
                    lock = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        lock = False
        pygame.quit()

    def rotation(self):
        """Tourne l'image d'un quart de tour vers la droite par la méthode de force brute,
        c'est-à-dire en parcourant tous les pixels de l'image (pixel par pixel).
        """
        # Cette fonction est la réponse à la question 1.a)
        # qui porte sur le traitement de l'image "buffon.png" de taille 512x512
        image = [[0] * 512 for i in range(512)]
        for x in range(512):
            for y in range(512):
                image[x][y] = self.window.get_at((x, y))
        image_rotation = [[0] * 512 for i in range(512)]
        # image_rotation correspond à l'ensemble des valeurs des pixels de l'image tournée à droite.
        for x in range(512):
            for y in range(512):
                image_rotation[x][y] = image[y][511 - x]
                # chaque pixel de coordonnées (x;y) devient ici
                # un nouveau pixel de coordonnées (y;-x)
                # d'une image retournée à droite.
                self.window.set_at((x, y), image_rotation[x][y])
        # mise à jour de l'affichage
        pygame.display.update()
        # Par ailleurs : Question 1.b) :
        # "Sachant qu’un pixel est représenté par quatre nombres entiers
        # compris entre 0 et 255 (rouge, vert, bleu et transparence),
        # estimez le coût supplémentaire en mémoire (en Mo) de cette méthode rotation."
        # Réponse :
        # en sachant qu'un pixel porte 4 information de taille d'un octet
        # (car les nombres compris entre 0 et 255
        # peuvent être représentés par 1 octet soit 8 bits)
        # Dans un tableau à 512 lignes et 512 colonnes, il va nous falloir
        # stocker 512^2 = 262144 octets, soit environs 0.26 Mo


Main()
