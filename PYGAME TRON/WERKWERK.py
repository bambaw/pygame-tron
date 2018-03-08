while True:
        countdown = 0
        restart = True
        while restart:
                import pygame
                import os
                os.environ["SDL_VIDEO_CENTERED"]="1"
                pygame.init()

                #RESOLUTION
                width, height = 1000 , 700
                gameDisplay = pygame.display.set_mode((width,height))

                #Wall arrays
                p1t = []
                p2t = []
                p3t = []
                p4t = []
                p1temp = []
                p2temp = []
                p3temp = []
                p4temp = []
                p1tempt = []
                p2tempt = []
                p3tempt = []
                p4tempt = []
                reps = 0
                
                #COLORS
                blue = (0, 128, 255)
                red = (255, 0, 0)
                orange = (255, 153, 0)
                violet = (102, 51, 153)

                def coll(x,y):
                        coll = pygame.Rect.colliderect(x,y)
                        return coll
                class P1T(object):    
                    def __init__(self, pos):
                        p1tempt.append(self)
                        self.rect = pygame.Rect(pos[0], pos[1], 10, 10)
                class P2T(object):    
                    def __init__(self, pos):
                        p2tempt.append(self)
                        self.rect = pygame.Rect(pos[0], pos[1], 10, 10)
                class P3T(object):    
                    def __init__(self, pos):
                        p3tempt.append(self)
                        self.rect = pygame.Rect(pos[0], pos[1], 10, 10)
                class P4T(object):    
                    def __init__(self, pos):
                        p4tempt.append(self)
                        self.rect = pygame.Rect(pos[0], pos[1], 10, 10)

                #PLAYER 1 COORDINATES
                x1 , y1 = 30 , 30
                p1moving = True

                #PLAYER 2 COORDINATES
                x2 , y2 = width - 40 , 30
                p2moving = True

                #PLAYER 3 COORDINATES
                x3 , y3 = 30 , height - 40
                p3moving = True

                #PLAYER 4 COORDINATES
                x4 , y4 = width - 40 , height - 40
                p4moving = True


                #MOVEMENT STR (w-up, a-left, s-down, d-right)
                p1m = "s"
                p2m = "a"
                p3m = "d"
                p4m = "w"

                #CLOCK, BACKGROUND, MUSIC
                clock = pygame.time.Clock()
                background_image = pygame.image.load("bg.jpg").convert()
                bg = gameDisplay.blit(background_image, [0,0])
                pygame.mixer.music.load("Albedo.mp3")
                pygame.mixer.music.play(loops = 0, start = 3.5)
                
                #Game Borders
                w_up = pygame.draw.rect(gameDisplay, (255,255,255), pygame.Rect(0,0,width,10))
                w_left = pygame.draw.rect(gameDisplay, (255,255,255), pygame.Rect(0,0,10,height))
                w_right = pygame.draw.rect(gameDisplay, (255,255,255) , pygame.Rect(width-10,0,10,height))
                w_down = pygame.draw.rect(gameDisplay, (255,255,255), pygame.Rect(0,height-10,width,10))

                #Player Initial Drawing
                p1hb = pygame.draw.rect(gameDisplay, blue, pygame.Rect(x1, y1, 10, 10))
                p2hb = pygame.draw.rect(gameDisplay, red, pygame.Rect(x2, y2, 10, 10))
                p3hb = pygame.draw.rect(gameDisplay, orange, pygame.Rect(x3, y3, 10, 10))
                p4hb = pygame.draw.rect(gameDisplay, violet, pygame.Rect(x4, y4, 10, 10))
				
				
                #def game_Loop():
                while countdown == 0:        
                        for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                                        done = True
                                        restart = False
                                        pygame.mixer.music.stop()
                                        pygame.display.quit()
                                if event.type == pygame.QUIT:
                                        done = True
                                        restart = False
                                        pygame.mixer.music.stop()
                                        pygame.display.quit()
                                #MUSIC CONTROLS
                                if event.type == pygame.KEYDOWN and event.key == pygame.K_KP1:
                                        pygame.mixer.music.pause()
                                if event.type == pygame.KEYDOWN and event.key == pygame.K_KP0:
                                        pygame.mixer.music.unpause()   
                                      

                        #DRAW PLAYERS
                        P1T((x1,y1))
                        p1hb = pygame.draw.rect(gameDisplay, blue, pygame.Rect(x1, y1, 10, 10))
                        for trail in p1t:
                                pygame.draw.rect(gameDisplay, blue, trail.rect)

                        P2T((x2,y2))
                        p2hb = pygame.draw.rect(gameDisplay, red, pygame.Rect(x2, y2, 10, 10))
                        for trail in p2t:
                                pygame.draw.rect(gameDisplay, red, trail.rect)

                        P3T((x3,y3))
                        p3hb = pygame.draw.rect(gameDisplay, orange, pygame.Rect(x3, y3, 10, 10))
                        for trail in p3t:
                                pygame.draw.rect(gameDisplay, orange, trail.rect)

                        P4T((x4,y4))
                        p4hb = pygame.draw.rect(gameDisplay, violet, pygame.Rect(x4, y4, 10, 10))
                        for trail in p4t:
                                pygame.draw.rect(gameDisplay, violet, trail.rect)

                        #GET KEYPRESSES
                        pressed = pygame.key.get_pressed()

                        #PLAYER CONTROLS
                        if p1moving == True:
                                if pressed[pygame.K_w] and p1m != "s" and p1m != "w": p1m = "w"
                                if pressed[pygame.K_a] and p1m != "d" and p1m != "a": p1m = "a"
                                if pressed[pygame.K_s] and p1m != "w" and p1m != "s": p1m = "s"
                                if pressed[pygame.K_d] and p1m != "a" and p1m != "d": p1m = "d"
                        if p2moving == True:
                                if pressed[pygame.K_UP] and p2m != "s" and p2m != "w": p2m = "w"
                                if pressed[pygame.K_LEFT] and p2m != "d" and p2m != "a": p2m = "a"
                                if pressed[pygame.K_DOWN] and p2m != "w" and p2m != "s": p2m = "s"                        
                                if pressed[pygame.K_RIGHT] and p2m != "a" and p2m != "d": p2m = "d"
                        if p3moving == True:
                                if pressed[pygame.K_t] and p3m != "s" and p3m != "w": p3m = "w"
                                if pressed[pygame.K_f] and p3m != "d" and p3m != "a": p3m = "a"
                                if pressed[pygame.K_g] and p3m != "w" and p3m != "s": p3m = "s"                        
                                if pressed[pygame.K_h] and p3m != "a" and p3m != "d": p3m = "d"
                        if p4moving == True:
                                if pressed[pygame.K_i] and p4m != "s" and p4m != "w": p4m = "w"
                                if pressed[pygame.K_j] and p4m != "d" and p4m != "a": p4m = "a"
                                if pressed[pygame.K_k] and p4m != "w" and p4m != "s": p4m = "s"                        
                                if pressed[pygame.K_l] and p4m != "a" and p4m != "d": p4m = "d"
								
                        #PlayerMoves
                        if p1moving == True:
                                if p1m == "w":
                                        y1 -= 4
                                if p1m == "a":
                                        x1 -= 4
                                if p1m == "s":
                                        y1 += 4
                                if p1m == "d":
                                        x1 += 4
                        if p2moving == True:
                                if p2m == "w":
                                        y2 -= 4
                                if p2m == "a":
                                        x2 -= 4
                                if p2m == "s":
                                        y2 += 4
                                if p2m == "d":
                                        x2 += 4
                        if p3moving == True:
                                if p3m == "w":
                                        y3 -= 4
                                if p3m == "a":
                                        x3 -= 4
                                if p3m == "s":
                                        y3 += 4
                                if p3m == "d":
                                        x3 += 4
                        if p4moving == True:
                                if p4m == "w":
                                        y4 -= 4
                                if p4m == "a":
                                        x4 -= 4
                                if p4m == "s":
                                        y4 += 4
                                if p4m == "d":
                                        x4 += 4
										
                        #CHECK COLLISION P2P
                        if coll(p1hb,p2hb):
                                p1moving = False
                                p2moving = False

                        #CHECK COLLISION P2W
                        if coll(p1hb,w_up) or coll(p1hb,w_left) or coll(p1hb,w_down) or coll(p1hb,w_right):
                                p1moving = False
                        if coll(p2hb,w_up) or coll(p2hb,w_left) or coll(p2hb,w_down) or coll(p2hb,w_right):
                                p2moving = False
                        if coll(p3hb,w_up) or coll(p3hb,w_left) or coll(p3hb,w_down) or coll(p3hb,w_right):
                                p3moving = False
                        if coll(p4hb,w_up) or coll(p4hb,w_left) or coll(p4hb,w_down) or coll(p4hb,w_right):
                                p4moving = False

                        #CHECK COLLISION P2T
                        for trail in p1t:
                                if coll(p1hb,trail.rect):
                                        p1moving = False
                                if coll(p2hb,trail.rect):
                                        p2moving = False
                                if coll(p3hb,trail.rect):
                                        p3moving = False
                                if coll(p4hb,trail.rect):
                                        p4moving = False
                        for trail in p2t:
                                if coll(p1hb,trail.rect):
                                        p1moving = False
                                if coll(p2hb,trail.rect):
                                        p2moving = False
                                if coll(p3hb,trail.rect):
                                        p3moving = False
                                if coll(p4hb,trail.rect):
                                        p4moving = False
                        for trail in p3t:
                                if coll(p1hb,trail.rect):
                                        p1moving = False
                                if coll(p2hb,trail.rect):
                                        p2moving = False
                                if coll(p3hb,trail.rect):
                                        p3moving = False
                                if coll(p4hb,trail.rect):
                                        p4moving = False
                        for trail in p4t:
                                if coll(p1hb,trail.rect):
                                        p1moving = False
                                if coll(p2hb,trail.rect):
                                        p2moving = False
                                if coll(p3hb,trail.rect):
                                        p3moving = False
                                if coll(p4hb,trail.rect):
                                        p4moving = False
                        
                        #TRAIL REPEAT
                        reps += 1
                        if reps == 4:
                                p1t.extend(p1temp)
                                p1temp = []
                                p2t.extend(p2temp)
                                p2temp = []
                                p3t.extend(p3temp)
                                p3temp = []
                                p4t.extend(p4temp)
                                p4temp = []
                                p1temp.extend(p1tempt)
                                p1tempt = []
                                p2temp.extend(p2tempt)
                                p2tempt = []
                                p3temp.extend(p3tempt)
                                p3tempt = []
                                p4temp.extend(p4tempt)
                                p4tempt = []
                                reps = 0
                        
                        pygame.display.flip()
                        clock.tick(60)
                        
                clock.tick(1)
