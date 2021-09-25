import pygame
import numpy as np

def boring_pi(d):
    S = d**2
    C = 0
    Cx = d/2
    Cy = d/2
    for i in range(d):
        for j in range(d):
            if ((i-Cx)**2)+((j-Cy)**2) < (d/2)**2:
                C+=1
    print(C*4/S)

pygame.init()

fontSize = 30
sysFont = pygame.font.SysFont(None, fontSize)

def textObjects(font,text,color):
    textSureface = font.render(text,True,color)
    return textSureface, textSureface.get_rect()

def message2screen(scr,msg,color = (20,20,20),x=2,y=2,font=sysFont):
    textSurf,textRect = textObjects(font,msg,color)
    textRect.topleft = x, y
    scr.blit(textSurf,textRect)

boring_pi(200)

rad = 200
size = rad*2

display = pygame.display.set_mode((size,size+fontSize))
display.fill((51,51,51))

dots = 0
dinc = 0
loop = True
im = 0
while loop:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                loop = False
    for _ in range(2000):            
        x,y = np.random.randint(0,rad*2,2)
        dots += 1  
        if (x-rad)**2+(y-rad)**2 <= rad*rad:
            dinc +=1
            pygame.draw.circle(display,(20,255,20),(x,y),1)
        else:
            pygame.draw.circle(display,(20,20,250),(x,y),1)
            
    #print("pi = ",4*dinc/dots)
    display.fill((51,51,51),(0,size,size,fontSize))
    message2screen(display,f"pi = {4*dinc/dots}",(250,250,250),5,size+5)

    pygame.display.update()
    
    if im < 100:
        pygame.image.save(display,f"gif/image{im}.png")
        im+=1
        
pygame.quit()
