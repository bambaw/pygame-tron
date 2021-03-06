import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
done = False

#PLAYER 1 COORDINATES
x1 = 30
y1 = 30

#PLAYER 2 COORDINATES
x2 = 1220
y2 = 30

clock = pygame.time.Clock()

background_image = pygame.image.load("bg.jpg").convert()
pygame.mixer.music.load("Albedo.mp3")
pygame.mixer.music.play(loops = 0, start = 3.5)

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.mixer.music.stop()
                        done = True
                        
                #CHANGE COLORS
                if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                        pygame.mixer.music.pause()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_KP0:
                        pygame.mixer.music.unpause()
        
        pressed = pygame.key.get_pressed()

        #PLAYER 1 CONTROLS
        if pressed[pygame.K_w]: y1 -= 1
        if pressed[pygame.K_a]: x1 -= 1
        if pressed[pygame.K_s]: y1 += 1
        if pressed[pygame.K_d]: x1  += 1

        #PLAYER 2 CONTROLS
        if pressed[pygame.K_UP]: y2 -= 1
        if pressed[pygame.K_LEFT]: x2 -= 1
        if pressed[pygame.K_DOWN]: y2 += 1
        if pressed[pygame.K_RIGHT]: x2  += 1

        #COLORS
        color1 = (0, 128, 255)
        color2 = (255, 0, 0)
        
        screen.fill((255, 255, 255))
        walls = pygame.draw.rect(screen, (0,0,0), pygame.Rect(0,0,1280,720) , 30)
        screen.blit(background_image, [0,0])

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
