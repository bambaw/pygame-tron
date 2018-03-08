import pygame

def coll(x,y):
        coll = pygame.Rect.colliderect(x,y)
        return coll

pygame.init()
screen = pygame.display.set_mode((1280, 720))
done = False

#PLAYER 1 COORDINATES
x1 = 30
y1 = 30
p1moving = True

#PLAYER 2 COORDINATES
x2 = 1220
y2 = 30
p2moving = True


#MOVEMENT STR
p1m = "s"
p2m = "a"

clock = pygame.time.Clock()

background_image = pygame.image.load("bg.jpg").convert()
pygame.mixer.music.load("Albedo.mp3")
pygame.mixer.music.play(loops = 0, start = 3.5)
#screen.blit(background_image, [0,0])

while not done:
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        pygame.mixer.music.stop()
                        pygame.display.quit()
                        done = True
                if event.type == pygame.QUIT:
                        pygame.mixer.music.stop()
                        pygame.display.quit()
                        done = True
                        
                #CHANGE COLORS
                if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                        pygame.mixer.music.pause()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_KP0:
                        pygame.mixer.music.unpause()

        #COLORS
        color1 = (0, 128, 255)
        color2 = (255, 0, 0)
        
        screen.blit(background_image, [0,0])
        w_up = pygame.draw.rect(screen, (100,0,100), pygame.Rect(0,0,1280,20))
        w_left = pygame.draw.rect(screen, (100,0,100), pygame.Rect(0,0,20,720))
        w_right = pygame.draw.rect(screen, (100,0,100) , pygame.Rect(1260,0,20,720))
        w_down = pygame.draw.rect(screen, (100,0,100), pygame.Rect(0,700,1280,20))


        #DRAW PLAYER 1
        p1hb = pygame.draw.rect(screen, color1, pygame.Rect(x1-2, y1-2, 10, 10))    
        #p1cb = pygame.draw.rect(screen, color1, pygame.Rect(x1, y1, 20, 20))

        #DRAW PLAYER 2
        p2hb = pygame.draw.rect(screen, color2, pygame.Rect(x2-2, y2-2, 10, 10)) 
        #p2cb = pygame.draw.rect(screen, color2, pygame.Rect(x2, y2, 20, 20))

        pressed = pygame.key.get_pressed()

        #PLAYER 1 CONTROLS
        if p1moving == True:
                if pressed[pygame.K_w] and p1m != "s": p1m = "w"
                        #y1 -= 1
                if pressed[pygame.K_a] and p1m != "d": p1m = "a"
                        #x1 -= 1
                if pressed[pygame.K_s] and p1m != "w": p1m = "s"
                        #y1 += 1
                if pressed[pygame.K_d] and p1m != "a": p1m = "d"
                        #x1  += 1

        #PLAYER 2 CONTROLS
        if p2moving == True:
                if pressed[pygame.K_UP] and p2m != "s": p2m = "w"
                        #y2 -= 1
                if pressed[pygame.K_LEFT] and p2m != "d": p2m = "a"
                        #x2 -= 1
                if pressed[pygame.K_DOWN] and p2m != "w": p2m = "s"
                        #y2 += 1
                if pressed[pygame.K_RIGHT] and p2m != "a": p2m = "d"
                        #x2  += 1

        #PlayerMoves
        if p1moving == True:
                if p1m == "w":
                        y1 -= 1
                if p1m == "a":
                        x1 -= 1
                if p1m == "s":
                        y1 += 1
                if p1m == "d":
                        x1 += 1
        if p2moving == True:
                if p2m == "w":
                        y2 -= 1
                if p2m == "a":
                        x2 -= 1
                if p2m == "s":
                        y2 += 1
                if p2m == "d":
                        x2 += 1

        #CHECK COLLISION P2P
        if coll(p1hb,p2hb):
                p1moving = False
                p2moving = False

        #CHECK COLLISION P2W
        if coll(p1hb,w_up) or coll(p1hb,w_left) or coll(p1hb,w_down) or coll(p1hb,w_right):
                p1moving = False
        if coll(p2hb,w_up) or coll(p2hb,w_left) or coll(p2hb,w_down) or coll(p2hb,w_right):
                p2moving = False
   

        pygame.display.flip()
        clock.tick(240)
