import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
done = False

#COLORS BOOL
c1 = True
c2 = True

#PLAYER 1 COORDINATES
x1 = 30
y1 = 30

#PLAYER 2 COORDINATES
x2 = 1220
y2 = 30

clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                        
                #CHANGE COLORS
                if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                        c1 = not c1
                if event.type == pygame.KEYDOWN and event.key == pygame.K_KP0:
                        c2 = not c2
        
        pressed = pygame.key.get_pressed()

        #PLAYER 1 CONTROLS
        if pressed[pygame.K_w]: y1 -= 1
        if pressed[pygame.K_a]: x1 -= 1
        if pressed[pygame.K_s]: y1 += 1
        if pressed[pygame.K_d]: x1  += 1

        #PLAYER 2 CONTROLS
        if pressed[pygame.K_UP]: y2 -= spT
        if pressed[pygame.K_LEFT]: x2 -= spT
        if pressed[pygame.K_DOWN]: y2 += spT
        if pressed[pygame.K_RIGHT]: x2  += spT

        #COLORS
        if c1: color1 = (0, 128, 255)
        else: color1 = (255, 0, 0)
        if c2: color2 = (255, 0, 0)
        else: color2 = (0, 128, 255)
        
        screen.fill((255, 255, 255))
        walls = pygame.draw.rect(screen, (0,0,0), pygame.Rect(0,0,1280,720) , 30)


        #DRAW PLAYER 1
        p1hb = pygame.draw.rect(screen, (0,0,0), pygame.Rect(x1-2, y1-2, 24, 24))    
        p1Tp = pygame.draw.rect(screen, (0,0,0), pygame.Rect(x1-2, y1-2, 24 , 2))
        p1Lt = pygame.draw.rect(screen, (0,0,0), pygame.Rect(x1-2, y1-2, 2, 24))
        p1Bt = pygame.draw.rect(screen, (0,0,0), pygame.Rect(x1-2, y1+20, 24, 2))
        p1Rt = pygame.draw.rect(screen, (0,0,0), pygame.Rect(x1+20, y1-2, 2, 24)) 
        p1cb = pygame.draw.rect(screen, color1, pygame.Rect(x1, y1, 20, 20))

        #DRAW PLAYER 2
        p2hb = pygame.draw.rect(screen, (0,0,0), pygame.Rect(x2-2, y2-2, 24, 24))
        p2Tp = pygame.draw.rect(screen, (0,0,0), pygame.Rect(x2-2, y2-2, 24 , 2))
        p2Lt = pygame.draw.rect(screen, (0,0,0), pygame.Rect(x2-2, y2-2, 2, 24))
        p2Bt = pygame.draw.rect(screen, (0,0,0), pygame.Rect(x2-2, y2+20, 24, 2))
        p2Rt = pygame.draw.rect(screen, (0,0,0), pygame.Rect(x2+20, y2-2, 2, 24))        
        p2cb = pygame.draw.rect(screen, color2, pygame.Rect(x2, y2, 20, 20))

        #CHECK COLLISION
        if pygame.Rect.colliderect(p1Tp, p2Bt):
                if pressed[pygame.K_w]:
                        y1 += 1
                if pressed[pygame.K_DOWN]:
                        y2 -= 1
        if pygame.Rect.colliderect(p1Rt, p2Lt):
                if pressed[pygame.K_d]:
                        x1 -= 1
                if pressed[pygame.K_LEFT]:
                        x2 += 1
        if pygame.Rect.colliderect(p1Bt, p2Tp):
                if pressed[pygame.K_s]:
                        y1 -= 1
                if pressed[pygame.K_UP]:
                        y2 += 1
        if pygame.Rect.colliderect(p1Lt, p2Rt):
                if pressed[pygame.K_a]:
                        x1 += 1
                if pressed[pygame.K_RIGHT]:
                        x2 -= 1

        if pygame.Rect.colliderect(p1hb,walls) or pygame.Rect.colliderect(p2hb,walls):
                print("True")
        else:
                print("False")

               
        pygame.display.flip()
        clock.tick(240)
