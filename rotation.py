import pygame
from pygame.locals import *

class Main :

    def __init__(self):
        """ 
        Affiche l'image buffon.png dans une fenêtre pygame
        et applique la méthode rotation().
        """
        
        # initialisation de pygame
        pygame.init()
        self.window = pygame.display.set_mode((600, 600))

        # affichage de l'image
        image = pygame.image.load("buffon.png") # 512 par 512
        self.window.blit(image, (0, 0))
        pygame.display.update()
        
        # rotation de l'image
        self.rotation()
        
        # maintien de la fenêtre
        self.hold()
        

    def hold(self):
        """
        Maintient la fenêtre ouverte jusqu'à sa fermeture
        ou la pression de la touche 'Echap'."""
        lock = True
        while lock :
            events_list = pygame.event.get()
            for event in events_list :
                if event.type == QUIT :
                    lock = False
                if event.type == KEYDOWN :
                    if event.key == K_ESCAPE :
                        lock = False
        pygame.quit()
        

    def rotation(self):
        """ 
        Tourne l'image d'un quart de tour vers la droite.
        """
            
            
        """ Le code ci-dessous n'est qu'un exemple de manipulation des
            pixels. Il ne tourne PAS l'image dun quart de tour !"""
            
        t = 256
        #t=128
        for i in range(t):
            for j in range(t):
                tl = self.window.get_at((i, j))
                tr = self.window.get_at((i+t, j))
                br = self.window.get_at((i+t, j+t))
                bl = self.window.get_at((i, j+t))
                    
                self.window.set_at((i, j), bl)
                self.window.set_at((i+t, j), tl)
                self.window.set_at((i+t, j+t), tr)
                self.window.set_at((i, j+t), br)

            # mise à jour de l'affichage   
            #pygame.display.update()
        pygame.display.update()
    
Main()