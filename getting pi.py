import pygame
import numpy as np

# d=circle diameter
def boring_pi(d):
    S = d**2
    C = 0
    Cx = d/2
    Cy = d/2
    for i in range(d):
        for j in range(d):
            if ((i-Cx)**2)+((j-Cy)**2) < (d/2)**2:
                C+=1
    return C*4/S

def _text_objects(font,text,color):
    text_surface = font.render(text,True,color)
    return text_surface, text_surface.get_rect()

def message_to_screen(screen,msg,color = (20,20,20),x=2,y=2,font=SYSFONT):
    text_surf,text_rect = _text_objects(font,msg,color)
    text_rect.topleft = x, y
    screen.blit(text_surf,text_rect)

pygame.init()

FONTSIZE = 30
SYSFONT = pygame.font.SysFont(None, FONTSIZE)
RADIUS = 200
SIZE = RADIUS*2

print(boring_pi(RADIUS))

display = pygame.display.set_mode((SIZE,SIZE+FONTSIZE))
display.fill((51,51,51))

dots = 0
dots_circle = 0
loop = True
frame = 0
while loop:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                loop = False
    for _ in range(2000):            
        x,y = np.random.randint(0,RADIUS*2,2)
        dots += 1  
        if (x-RADIUS)**2+(y-RADIUS)**2 <= RADIUS*RADIUS:
            dots_circle +=1
            pygame.draw.circle(display,(20,255,20),(x,y),1)
        else:
            pygame.draw.circle(display,(20,20,250),(x,y),1)
            
    #print("pi = ",4*dots_circle/dots)
    display.fill((51,51,51),(0,SIZE,SIZE,FONTSIZE))
    message_to_screen(display,f"pi = {4*dots_circle/dots}",(250,250,250),5,SIZE+5)

    pygame.display.update()
    
    if frame < 100:
        pygame.image.save(display,f"gif/image{frame}.png")
        frame += 1
        
pygame.quit()
