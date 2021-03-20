import pygame


#definir une classe qui va s'occuper des animations 
class AnimateSprite(pygame.sprite.Sprite):
    #definir les choses à faire à la création de l'entité 
    def __init__(self,sprite_name, size=(200,200)): 
        super().__init__()
        self.size = size
        self.image = pygame.image.load('/assets/assets/'+ sprite_name + '.png')
        self.image = pygame.transform.scale(self.image,size)
        self.current_image = 0 #commencer l'anim à l'image 0 
        self.images = animation.get(sprite_name)
        self.animation = False
    #definir une methode por demarrer l'animation 
    def start_animation(self):
        self.animation = True

    #definir une methode pour animer le sprite 
    def animate(self,loop=False):
        #vérifier si l'animation est active 
        if self.animation : 
            #passer à l'image  suivante 
            self.current_image += 1 
            #vérifier si on a atteint la fin de l'animation 
            if self.current_image >= len(self.images):
                #remettre l'animation au départ 
                self.current_image = 0 
                #vérifier si l'aniamation n'est pas en mode boucle
                if  loop is False:
                    #désactivation de l'animation 
                    self.animation = False
            #modifier l'image précédente par la suivante 
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image,self.size)


#definir une fonction pour charger les images d'un sprite 
def load_animation_images(sprite_name):
    #charger les 24 images de ce sprite dans le dossier correspondant
    images = []
    #recuperer le chemin du dossier pour ce sprite 
    path = f'C:/Users/Emir Abid/Desktop/Emir/Coding/EXercice python/Project-Python/Python-Game/assets/assets/{sprite_name}/{sprite_name}'
    #boucler sur chaque image dans ce dossier
    for num in range(1,24):
        image_path =  path + str(num) + '.png'
        images.append( pygame.image.load(image_path))
    #renvoyer le  contenu de la liste d'images
    return images

#definir un dictionnaire qui va contenire les images chargées de chaque sprite
animation = {
    'mummy': load_animation_images('mummy'),
    'player': load_animation_images('player'),
    'alien': load_animation_images('alien')
}