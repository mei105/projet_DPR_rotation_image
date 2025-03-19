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
        

    def rotation_dpr(self, t,x,y):        
        """ 
        Tourne l'image d'un quart de tour vers la droite.
        Le code ci-dessous n'est qu'un exemple de manipulation des
        pixels. Il ne tourne PAS l'image dun quart de tour !"""
            
        if t>1 :

            self.rotation_dpr(t//2,x+t,y)
            self.rotation_dpr(t//2,x,y+t) 
            self.rotation_dpr(t//2,x+t,y+t)
            self.rotation_dpr(t//2,x,y)
        for j in range(x,x+t):
            for i in range(y,y+t):
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
        def rotation_dpr_perso(self,sens,t,x,y):        
            """ 
            Tourne l'image d'un quart de tour vers la droite.
            Le code ci-dessous n'est qu'un exemple de manipulation des
            pixels. Il ne tourne PAS l'image dun quart de tour !"""
                
            if t>1 :
    
                self.rotation_dpr_perso(sens,t//2,x+t,y)
                self.rotation_dpr_perso(sens,t//2,x,y+t) 
                self.rotation_dpr_perso(sens,t//2,x+t,y+t)
                self.rotation_dpr_perso(sens,t//2,x,y)
            if sens == 'l' :
                for j in range(x,x+t):
                    for i in range(y,y+t):
                        tl = self.window.get_at((i, j))
                        tr = self.window.get_at((i+t, j))
                        br = self.window.get_at((i+t, j+t))
                        bl = self.window.get_at((i, j+t))
                        
                            
                        self.window.set_at((i, j), tr)
                        self.window.set_at((i+t, j), br)
                        self.window.set_at((i+t, j+t), bl)
                        self.window.set_at((i, j+t), tl)
            if sens == 'r' :
                for j in range(x,x+t):
                    for i in range(y,y+t):
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
        
        def rotation_brut(self):
        """ 
        Tourne l'image d'un quart de tour vers la droite.
        """
        image = [[0] * 512 for i in range(512)]
        for x in range(512):
            for y in range(512):
                image[x][y] = self.window.get_at((x, y))
        #print(image)
        image_rot = [[0] * 512 for i in range(512)]
        for x in range(512):
            for y in range(512):
                image_rot[x][y] = image[y][511-x]
                self.window.set_at((x,y),image_rot[x][y])
        pygame.display.update()
        
    
Main()
