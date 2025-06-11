import pygame
pygame.init()
tela  = pygame.display.set_mode((1080,720))



         
run = True         
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run  = False
            pygame.quit()
    tela.fill('black')  
    pygame.draw.rect(tela,('purple'),(300,200,70,70))
    pygame.display.flip()    
    # CIRCULO
    pygame.draw.circle(tela,('green'),(200,150,),54)
    pygame.display.flip()

    # ELIPSE
    pygame.draw.ellipse(tela,('blue'),(400, 100, 459,100))
    pygame.display.flip()